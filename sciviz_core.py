# sciviz_edu/core/scene.py
"""
Core educational scene class extending Manim with interactive capabilities
"""

from manim import *
from typing import List, Dict, Any, Callable, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
import numpy as np
import json
from pathlib import Path


class BloomLevel(Enum):
    """Bloom's Taxonomy cognitive levels"""
    REMEMBER = 1
    UNDERSTAND = 2
    APPLY = 3
    ANALYZE = 4
    EVALUATE = 5
    CREATE = 6


class DifficultyLevel(Enum):
    """Content difficulty levels"""
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    EXPERT = 4
    
    def next(self):
        members = list(DifficultyLevel)
        idx = members.index(self)
        return members[min(idx + 1, len(members) - 1)]
    
    def previous(self):
        members = list(DifficultyLevel)
        idx = members.index(self)
        return members[max(idx - 1, 0)]


class InteractionType(Enum):
    """Types of interactive elements"""
    SLIDER = "slider"
    BUTTON = "button"
    TOGGLE = "toggle"
    INPUT = "input"
    DROPDOWN = "dropdown"
    CANVAS = "canvas"


@dataclass
class LearningObjective:
    """Specific learning outcome"""
    id: str
    description: str
    bloom_level: BloomLevel
    assessment_method: str
    success_criteria: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)


@dataclass
class Concept:
    """Represents a scientific concept"""
    id: str
    name: str
    definition: str
    examples: List[str] = field(default_factory=list)
    prerequisites: List[str] = field(default_factory=list)
    related: List[str] = field(default_factory=list)
    difficulty: DifficultyLevel = DifficultyLevel.INTERMEDIATE
    bloom_level: BloomLevel = BloomLevel.UNDERSTAND


@dataclass
class InteractiveElement:
    """Interactive component within a scene"""
    id: str
    type: InteractionType
    label: str
    target: str  # What parameter it controls
    range: Optional[Tuple[float, float]] = None
    default: Any = None
    callback: Optional[str] = None  # Method name as string
    learning_hook: Optional[str] = None  # Links to learning objective
    description: str = ""


@dataclass
class Question:
    """Assessment question"""
    id: str
    text: str
    type: str  # "multiple_choice", "true_false", "numeric", "short_answer"
    options: Optional[List[str]] = None
    correct_answer: Any = None
    points: int = 1
    explanation: str = ""


@dataclass
class AssessmentCheckpoint:
    """Assessment point within a scene"""
    timestamp: float
    question: Question
    feedback_correct: str
    feedback_incorrect: str
    hints: List[str] = field(default_factory=list)
    related_concepts: List[str] = field(default_factory=list)


@dataclass
class NarrativeSegment:
    """Narrative/subtitle segment"""
    start_time: float
    end_time: float
    text: str
    position: str = "bottom"  # "top", "bottom", "left", "right", "center"
    style: Dict[str, Any] = field(default_factory=dict)


class EducationalScene(Scene):
    """
    Enhanced Manim scene with educational features:
    - Learning objectives tracking
    - Interactive elements
    - Assessment checkpoints
    - Narrative management
    - Knowledge graph integration
    - Export to interactive web format
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Educational metadata
        self.scene_id = self.__class__.__name__
        self.title = ""
        self.description = ""
        self.duration = 0
        
        # Learning components
        self.objectives: List[LearningObjective] = []
        self.concepts: List[Concept] = []
        self.prerequisites: List[str] = []
        self.difficulty = DifficultyLevel.INTERMEDIATE
        
        # Interactive components
        self.interactions: List[InteractiveElement] = []
        self.interactive_state: Dict[str, Any] = {}
        
        # Assessment components
        self.assessments: List[AssessmentCheckpoint] = []
        self.quiz_results: Dict[str, bool] = {}
        
        # Narrative components
        self.narrative: List[NarrativeSegment] = []
        self.current_subtitle = None
        
        # Export data
        self.export_data = {
            "metadata": {},
            "timeline": [],
            "interactions": [],
            "assessments": []
        }
    
    # ============================================
    # Learning Objective Management
    # ============================================
    
    def add_objective(self, objective: LearningObjective):
        """Add a learning objective to the scene"""
        self.objectives.append(objective)
        return objective
    
    def set_difficulty(self, level: DifficultyLevel):
        """Set overall difficulty level"""
        self.difficulty = level
    
    def add_concept(self, concept: Concept):
        """Add a concept covered in this scene"""
        self.concepts.append(concept)
        return concept
    
    def add_prerequisite(self, prereq_id: str):
        """Add a prerequisite scene or concept"""
        self.prerequisites.append(prereq_id)
    
    # ============================================
    # Interactive Elements
    # ============================================
    
    def add_slider(
        self,
        name: str,
        range: Tuple[float, float],
        default: float,
        callback: Callable,
        label: str = "",
        description: str = "",
        learning_hook: Optional[str] = None
    ) -> InteractiveElement:
        """Add a slider control"""
        element = InteractiveElement(
            id=f"slider_{name}",
            type=InteractionType.SLIDER,
            label=label or name,
            target=name,
            range=range,
            default=default,
            callback=callback.__name__ if callable(callback) else callback,
            learning_hook=learning_hook,
            description=description
        )
        self.interactions.append(element)
        self.interactive_state[name] = default
        return element
    
    def add_button(
        self,
        name: str,
        callback: Callable,
        label: str = "",
        description: str = ""
    ) -> InteractiveElement:
        """Add a button control"""
        element = InteractiveElement(
            id=f"button_{name}",
            type=InteractionType.BUTTON,
            label=label or name,
            target=name,
            callback=callback.__name__ if callable(callback) else callback,
            description=description
        )
        self.interactions.append(element)
        return element
    
    def add_toggle(
        self,
        name: str,
        default: bool,
        callback: Callable,
        label: str = "",
        description: str = ""
    ) -> InteractiveElement:
        """Add a toggle switch"""
        element = InteractiveElement(
            id=f"toggle_{name}",
            type=InteractionType.TOGGLE,
            label=label or name,
            target=name,
            default=default,
            callback=callback.__name__ if callable(callback) else callback,
            description=description
        )
        self.interactions.append(element)
        self.interactive_state[name] = default
        return element
    
    def wait_for_interaction(self, timeout: float = None):
        """Pause animation until user interaction (or timeout)"""
        # In static render, this becomes a normal wait
        # In interactive mode, this signals a pause point
        marker = Dot(radius=0, color=BLUE).set_opacity(0)
        marker.interaction_point = True
        self.add(marker)
        self.wait(timeout or 5)
        self.remove(marker)
    
    # ============================================
    # Assessment
    # ============================================
    
    def add_checkpoint(
        self,
        timestamp: float,
        question: str,
        correct: Any,
        question_type: str = "multiple_choice",
        options: Optional[List[str]] = None,
        feedback_correct: str = "Correct!",
        feedback_incorrect: str = "Not quite. Try again.",
        hints: Optional[List[str]] = None,
        related_concepts: Optional[List[str]] = None,
        explanation: str = ""
    ) -> AssessmentCheckpoint:
        """Add an assessment checkpoint"""
        q = Question(
            id=f"q_{len(self.assessments)}",
            text=question,
            type=question_type,
            options=options,
            correct_answer=correct,
            explanation=explanation
        )
        
        checkpoint = AssessmentCheckpoint(
            timestamp=timestamp,
            question=q,
            feedback_correct=feedback_correct,
            feedback_incorrect=feedback_incorrect,
            hints=hints or [],
            related_concepts=related_concepts or []
        )
        
        self.assessments.append(checkpoint)
        return checkpoint
    
    def add_quiz(self, questions: List[Question], timestamp: float):
        """Add multiple questions as a quiz"""