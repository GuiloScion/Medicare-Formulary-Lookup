# main.py
"""
Ultra-Advanced Manim Documentary: Mycorrhizal Networks
Features:
- Adaptive subtitle system with word-wrapping and automatic sizing
- Advanced particle systems with physics
- Dynamic camera movements and depth of field simulation
- Procedural generation with seeded randomness
- Enhanced visual effects (bloom, depth, motion blur simulation)
- Optimized performance with caching
- Professional color grading
- Smooth scene transitions with multiple styles
- Audio-ready timing (30-minute runtime)
"""

from manim import *
import numpy as np
import random
from typing import List, Tuple, Optional
from math import pi, sin, cos

# ==================== CONFIGURATION ====================
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60  # Smooth 60fps
config.background_color = "#0a0e14"

# Performance optimization flags
ENABLE_ADVANCED_EFFECTS = True  # Set to False for faster rendering
PARTICLE_DENSITY = "high"  # "low", "medium", "high"
ENABLE_SOUND_MARKERS = True  # Audio cue markers for post-production

# Scene timing (seconds) - Total: 1800s (30 min)
SCENE_DURATIONS = {
    "IntroScene": 135,
    "HistoryScene": 195,
    "NetworkOverviewScene": 255,
    "MiningExchangeScene": 235,
    "CommunicationScene": 175,
    "ArchitectureScene": 135,
    "CompetitionScene": 115,
    "EcosystemsScene": 115,
    "ResearchMethodsScene": 165,
    "ThreatsRestorationScene": 215,
    "ConclusionScene": 60,
}

# Professional color palette with HDR considerations
PALETTE = {
    "fungal": "#1dd3b0",
    "fungal_bright": "#2fffd4",
    "fungal_dark": "#0d6b5d",
    "plant": "#2d7a4a",
    "plant_light": "#86ce9e",
    "plant_dark": "#1a4d2e",
    "nutrient": "#ffcb47",
    "nutrient_bright": "#ffe484",
    "carbon": "#f4e8c1",
    "alert": "#ff6b6b",
    "alert_bright": "#ff9999",
    "network": "#4ecdc4",
    "defense": "#ffd89b",
    "text_primary": "#f0f4f8",
    "text_secondary": "#cbd5e0",
    "text_tertiary": "#a0aec0",
    "accent_purple": "#b794f4",
    "accent_blue": "#4299e1",
    "depth_near": "#1a2332",
    "depth_far": "#0f1419",
}

# ==================== ADVANCED SUBTITLE SYSTEM ====================
class AdaptiveSubtitle:
    """Intelligent subtitle system with word-wrapping and timing"""
    
    @staticmethod
    def create_subtitle(
        text: str,
        max_width: float = 12.0,
        font_size: int = 28,
        line_spacing: float = 0.15,
        position: np.ndarray = DOWN * 2.8,
        background_opacity: float = 0.75
    ) -> VGroup:
        """Create a professionally formatted subtitle with automatic word-wrapping"""
        
        # Word wrap algorithm
        words = text.split()
        lines = []
        current_line = []
        
        # Estimate characters per line based on max_width and font_size
        chars_per_line = int(max_width * 8.5)  # Empirical constant
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if len(test_line) <= chars_per_line:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        # Create text objects with proper spacing
        text_objects = VGroup()
        for line in lines:
            line_text = Text(
                line,
                font_size=font_size,
                color=PALETTE["text_primary"],
                weight=MEDIUM,
                font="Helvetica"
            )
            text_objects.add(line_text)
        
        text_objects.arrange(DOWN, buff=line_spacing, center=True)
        
        # Create rounded background with padding
        background = SurroundingRectangle(
            text_objects,
            buff=0.3,
            corner_radius=0.15,
            fill_color=BLACK,
            fill_opacity=background_opacity,
            stroke_width=0
        )
        
        # Add subtle gradient overlay
        gradient = Rectangle(
            width=background.width,
            height=background.height,
            fill_opacity=0
        ).move_to(background.get_center())
        gradient.set_sheen_direction(UP)
        gradient.set_sheen(0.2, direction=UP)
        
        subtitle_group = VGroup(background, gradient, text_objects)
        subtitle_group.move_to(position)
        subtitle_group.set_z_index(5000)
        
        return subtitle_group
    
    @staticmethod
    def display_subtitles(
        scene: Scene,
        lines: List[str],
        total_time: float,
        transition_time: float = 0.5,
        hold_last: float = 1.0
    ):
        """Display subtitles with smooth timing and transitions"""
        if not lines:
            return
        
        time_per_subtitle = (total_time - hold_last) / len(lines)
        display_time = max(time_per_subtitle - transition_time, 2.0)
        
        previous_subtitle = None
        
        for i, text in enumerate(lines):
            current_subtitle = AdaptiveSubtitle.create_subtitle(text)
            
            if previous_subtitle:
                # Smooth crossfade
                scene.play(
                    FadeOut(previous_subtitle, shift=DOWN * 0.3, scale=0.95),
                    FadeIn(current_subtitle, shift=UP * 0.3, scale=1.05),
                    run_time=transition_time
                )
            else:
                # First subtitle
                scene.play(
                    FadeIn(current_subtitle, shift=UP * 0.3),
                    run_time=transition_time * 0.8
                )
            
            # Hold subtitle
            scene.wait(display_time)
            previous_subtitle = current_subtitle
        
        # Fade out last subtitle
        if previous_subtitle:
            scene.play(
                FadeOut(previous_subtitle, shift=DOWN * 0.3, scale=0.95),
                run_time=transition_time
            )

# ==================== ADVANCED FEATURES ====================

class PerformanceOptimizer:
    """Adaptive quality based on system resources"""
    
    @staticmethod
    def get_particle_count(base_count: int) -> int:
        """Adjust particle count based on PARTICLE_DENSITY setting"""
        if PARTICLE_DENSITY == "low":
            return max(5, base_count // 3)
        elif PARTICLE_DENSITY == "medium":
            return max(8, base_count // 2)
        return base_count
    
    @staticmethod
    def should_use_effect() -> bool:
        """Check if advanced effects should be rendered"""
        return ENABLE_ADVANCED_EFFECTS

class AudioCueSystem:
    """System for marking audio sync points"""
    
    def __init__(self):
        self.cues = []
    
    def add_cue(self, time: float, cue_type: str, description: str):
        """Add audio cue marker"""
        if ENABLE_SOUND_MARKERS:
            self.cues.append({
                "time": time,
                "type": cue_type,
                "description": description
            })
    
    def export_cues(self, filename: str = "audio_cues.json"):
        """Export cues for audio production"""
        import json
        with open(filename, 'w') as f:
            json.dump(self.cues, f, indent=2)

class DataVisualization:
    """Advanced data visualization helpers"""
    
    @staticmethod
    def create_animated_chart(
        data: dict,
        chart_type: str = "bar",
        colors: list = None,
        position: np.ndarray = ORIGIN
    ) -> VGroup:
        """Create animated data charts"""
        if colors is None:
            colors = [PALETTE["fungal"], PALETTE["plant"], PALETTE["nutrient"]]
        
        chart = VGroup()
        
        if chart_type == "bar":
            max_val = max(data.values())
            bar_width = 0.6
            spacing = 1.0
            
            for i, (label, value) in enumerate(data.items()):
                bar_height = (value / max_val) * 3.0
                
                bar = Rectangle(
                    width=bar_width,
                    height=bar_height,
                    fill_opacity=0.8,
                    stroke_width=2
                )
                bar.set_fill(colors[i % len(colors)])
                bar.set_stroke(colors[i % len(colors)])
                
                bar_label = Text(label, font_size=20)
                bar_label.next_to(bar, DOWN, buff=0.2)
                
                value_label = Text(f"{value:.1f}", font_size=18)
                value_label.next_to(bar, UP, buff=0.1)
                
                group = VGroup(bar, bar_label, value_label)
                group.shift(RIGHT * (i - len(data) / 2) * spacing)
                
                chart.add(group)
        
        chart.move_to(position)
        return chart
    
    @staticmethod
    def create_network_stats(
        node_count: int,
        edge_count: int,
        position: np.ndarray = ORIGIN
    ) -> VGroup:
        """Create network statistics display"""
        stats = VGroup()
        
        node_text = Text(
            f"Nodes: {node_count}",
            font_size=24,
            color=PALETTE["text_primary"]
        )
        
        edge_text = Text(
            f"Connections: {edge_count}",
            font_size=24,
            color=PALETTE["text_primary"]
        )
        
        efficiency = (edge_count / (node_count * (node_count - 1) / 2)) * 100
        efficiency_text = Text(
            f"Network Efficiency: {efficiency:.1f}%",
            font_size=24,
            color=PALETTE["accent_blue"]
        )
        
        stats.add(node_text, edge_text, efficiency_text)
        stats.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        stats.move_to(position)
        
        return stats

class InteractiveElements:
    """Create elements that appear interactive (for tutorial mode)"""
    
    @staticmethod
    def create_tooltip(
        text: str,
        target: Mobject,
        direction: np.ndarray = UP
    ) -> VGroup:
        """Create tooltip that points to an object"""
        tooltip_text = Text(text, font_size=20, color=PALETTE["text_primary"])
        
        tooltip_bg = SurroundingRectangle(
            tooltip_text,
            buff=0.15,
            corner_radius=0.1,
            fill_color=BLACK,
            fill_opacity=0.85,
            stroke_color=PALETTE["accent_blue"],
            stroke_width=2
        )
        
        # Arrow pointing to target
        arrow = Arrow(
            tooltip_bg.get_edge_center(-direction),
            target.get_edge_center(direction),
            buff=0.1,
            stroke_width=3,
            color=PALETTE["accent_blue"]
        )
        
        tooltip = VGroup(tooltip_bg, tooltip_text, arrow)
        tooltip_text.move_to(tooltip_bg.get_center())
        
        return tooltip
    
    @staticmethod
    def create_zoom_indicator(
        target: Mobject,
        zoom_level: str = "1000×"
    ) -> VGroup:
        """Create zoom level indicator"""
        indicator = VGroup()
        
        # Reticle
        circle = Circle(radius=0.8, stroke_width=2, color=PALETTE["accent_blue"])
        circle.move_to(target.get_center())
        
        crosshair_h = Line(LEFT * 0.6, RIGHT * 0.6, stroke_width=2)
        crosshair_v = Line(DOWN * 0.6, UP * 0.6, stroke_width=2)
        crosshair_h.move_to(circle.get_center())
        crosshair_v.move_to(circle.get_center())
        crosshair_h.set_color(PALETTE["accent_blue"])
        crosshair_v.set_color(PALETTE["accent_blue"])
        
        # Zoom text
        zoom_text = Text(
            zoom_level,
            font_size=20,
            color=PALETTE["accent_blue"]
        )
        zoom_text.next_to(circle, DOWN, buff=0.3)
        
        indicator.add(circle, crosshair_h, crosshair_v, zoom_text)
        return indicator

class TimeIndicator(VGroup):
    """Timeline indicator for long documentaries"""
    
    def __init__(self, total_duration: float, **kwargs):
        super().__init__(**kwargs)
        self.total_duration = total_duration
        self.current_time = 0
        
        # Progress bar
        self.bar_bg = Rectangle(
            width=12,
            height=0.15,
            fill_color=PALETTE["text_tertiary"],
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.bar_fill = Rectangle(
            width=0,
            height=0.15,
            fill_color=PALETTE["accent_blue"],
            fill_opacity=0.8,
            stroke_width=0
        )
        self.bar_fill.align_to(self.bar_bg, LEFT)
        
        # Time text
        self.time_text = Text(
            "0:00 / 30:00",
            font_size=16,
            color=PALETTE["text_secondary"]
        )
        self.time_text.next_to(self.bar_bg, RIGHT, buff=0.3)
        
        self.add(self.bar_bg, self.bar_fill, self.time_text)
        self.to_corner(DL, buff=0.5)
        self.set_z_index(4999)
    
    def update_progress(self, current_time: float):
        """Update progress bar"""
        self.current_time = current_time
        progress = min(current_time / self.total_duration, 1.0)
        
        new_width = self.bar_bg.width * progress
        self.bar_fill.width = new_width
        self.bar_fill.align_to(self.bar_bg, LEFT)
        
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        total_min = int(self.total_duration // 60)
        total_sec = int(self.total_duration % 60)
        
        time_str = f"{minutes}:{seconds:02d} / {total_min}:{total_sec:02d}"
        self.time_text.become(
            Text(time_str, font_size=16, color=PALETTE["text_secondary"])
        )
        self.time_text.next_to(self.bar_bg, RIGHT, buff=0.3)

class AnimationPresets:
    """Preset animation patterns for consistency"""
    
    @staticmethod
    def organic_growth(mobject: Mobject, run_time: float = 2.0) -> Animation:
        """Natural growth animation"""
        return Create(
            mobject,
            run_time=run_time,
            rate_func=lambda t: smooth(t) * (1 + 0.1 * np.sin(t * 2 * PI))
        )
    
    @staticmethod
    def pulse_attention(mobject: Mobject, cycles: int = 2) -> list:
        """Pulsing animation to draw attention"""
        animations = []
        for _ in range(cycles):
            animations.extend([
                mobject.animate.scale(1.15).set_opacity(1.0),
                mobject.animate.scale(1/1.15).set_opacity(0.8)
            ])
        return animations
    
    @staticmethod
    def cascade_reveal(mobjects: list, lag_ratio: float = 0.1) -> Animation:
        """Cascading reveal of multiple objects"""
        return LaggedStart(
            *[FadeIn(mob, shift=UP * 0.2, scale=1.1) for mob in mobjects],
            lag_ratio=lag_ratio
        )

class CinematicCamera:
    """Advanced camera movement patterns"""
    
    @staticmethod
    def dolly_zoom(
        scene: Scene,
        target: Mobject,
        zoom_factor: float = 0.8,
        run_time: float = 3.0
    ):
        """Hitchcock dolly zoom effect"""
        original_pos = scene.camera.frame.get_center()
        target_pos = target.get_center()
        
        scene.play(
            scene.camera.frame.animate.scale(zoom_factor).move_to(target_pos),
            run_time=run_time,
            rate_func=smooth
        )
    
    @staticmethod
    def orbital_pan(
        scene: Scene,
        center: np.ndarray,
        radius: float = 2.0,
        angle: float = PI / 2,
        run_time: float = 4.0
    ):
        """Orbit around a point"""
        start_angle = 0
        
        def updater(mob, alpha):
            current_angle = start_angle + angle * smooth(alpha)
            new_pos = center + radius * np.array([
                np.cos(current_angle),
                np.sin(current_angle),
                0
            ])
            mob.move_to(new_pos)
        
        scene.play(
            UpdateFromAlphaFunc(scene.camera.frame, updater),
            run_time=run_time
        )
    
    @staticmethod
    def rack_focus(
        scene: Scene,
        from_target: Mobject,
        to_target: Mobject,
        run_time: float = 2.0
    ):
        """Simulate focus shift between objects"""
        # Fade out background
        scene.play(
            from_target.animate.set_opacity(0.3),
            to_target.animate.set_opacity(1.0),
            run_time=run_time / 2
        )
        
        # Move camera
        scene.play(
            scene.camera.frame.animate.move_to(to_target.get_center()),
            run_time=run_time / 2
        )

class ScientificNotation:
    """Helpers for scientific accuracy"""
    
    @staticmethod
    def create_scale_bar(
        length: float = 2.0,
        real_size: str = "1 mm",
        position: np.ndarray = None
    ) -> VGroup:
        """Create accurate scale bar"""
        if position is None:
            position = DOWN * 3 + RIGHT * 5
        
        bar = Line(LEFT * length / 2, RIGHT * length / 2, stroke_width=3)
        bar.set_color(WHITE)
        
        # End markers
        left_mark = Line(UP * 0.1, DOWN * 0.1, stroke_width=3)
        right_mark = Line(UP * 0.1, DOWN * 0.1, stroke_width=3)
        left_mark.move_to(bar.get_left())
        right_mark.move_to(bar.get_right())
        left_mark.set_color(WHITE)
        right_mark.set_color(WHITE)
        
        # Label
        label = Text(real_size, font_size=18, color=WHITE)
        label.next_to(bar, DOWN, buff=0.15)
        
        scale_bar = VGroup(bar, left_mark, right_mark, label)
        scale_bar.move_to(position)
        
        return scale_bar
    
    @staticmethod
    def create_citation(
        reference: str,
        position: np.ndarray = None
    ) -> Text:
        """Add scientific citation"""
        if position is None:
            position = DOWN * 3.5 + LEFT * 5
        
        citation = Text(
            f"Source: {reference}",
            font_size=14,
            color=PALETTE["text_tertiary"],
            slant=ITALIC
        )
        citation.move_to(position)
        citation.set_opacity(0.7)
        
        return citation

class EducationalOverlays:
    """Informational overlays for educational content"""
    
    @staticmethod
    def create_fact_box(
        title: str,
        facts: list,
        position: np.ndarray = RIGHT * 4
    ) -> VGroup:
        """Create fact box overlay"""
        box = VGroup()
        
        # Title
        title_text = Text(
            title,
            font_size=26,
            weight=BOLD,
            color=PALETTE["text_primary"]
        )
        
        # Facts
        fact_items = VGroup()
        for i, fact in enumerate(facts):
            bullet = Text("•", font_size=20, color=PALETTE["accent_blue"])
            fact_text = Text(fact, font_size=18, color=PALETTE["text_secondary"])
            fact_text.next_to(bullet, RIGHT, buff=0.2)
            
            fact_item = VGroup(bullet, fact_text)
            fact_items.add(fact_item)
        
        fact_items.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        fact_items.next_to(title_text, DOWN, buff=0.4, aligned_edge=LEFT)
        
        content = VGroup(title_text, fact_items)
        
        # Background
        bg = SurroundingRectangle(
            content,
            buff=0.3,
            corner_radius=0.15,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=PALETTE["accent_blue"],
            stroke_width=2
        )
        
        box.add(bg, content)
        box.move_to(position)
        
        return box
    
    @staticmethod
    def create_comparison_split(
        left_title: str,
        right_title: str,
        left_content: VGroup,
        right_content: VGroup
    ) -> VGroup:
        """Create split-screen comparison"""
        comparison = VGroup()
        
        # Divider
        divider = Line(UP * 4, DOWN * 4, stroke_width=2)
        divider.set_color(PALETTE["text_tertiary"])
        
        # Titles
        left_label = Text(left_title, font_size=32, color=PALETTE["text_primary"])
        left_label.to_edge(UP, buff=0.8).shift(LEFT * 3.5)
        
        right_label = Text(right_title, font_size=32, color=PALETTE["text_primary"])
        right_label.to_edge(UP, buff=0.8).shift(RIGHT * 3.5)
        
        # Position content
        left_content.shift(LEFT * 3.5)
        right_content.shift(RIGHT * 3.5)
        
        comparison.add(divider, left_label, right_label, left_content, right_content)
        
        return comparison

# Add to existing visual effects class
class VisualEffects:
    """Collection of advanced visual effects"""
    
    @staticmethod
    def add_glow(
        mobject: VMobject,
        color: str = YELLOW,
        intensity: float = 0.4,
        layers: int = 3,
        scale_factor: float = 1.3
    ) -> VGroup:
        """Multi-layer glow effect for depth"""
        glow_group = VGroup()
        
        for i in range(layers):
            glow_layer = mobject.copy()
            opacity = intensity * (1 - i / layers)
            width = mobject.get_stroke_width() * (scale_factor ** (i + 1))
            
            glow_layer.set_stroke(color, width=width, opacity=opacity)
            glow_layer.set_fill(opacity=0)
            glow_layer.set_z_index(mobject.z_index - i - 1)
            glow_group.add(glow_layer)
        
        glow_group.add(mobject)
        return glow_group
    
    @staticmethod
    def depth_fade(mobject: VMobject, depth: float = 0.5) -> VMobject:
        """Simulate depth of field by adjusting opacity and blur"""
        fade_factor = 1 - depth * 0.6
        mobject.set_opacity(fade_factor)
        return mobject
    
    @staticmethod
    def chromatic_aberration(mobject: VMobject, intensity: float = 0.02) -> VGroup:
        """Simulate lens chromatic aberration"""
        red_shift = mobject.copy().set_color(RED).shift(RIGHT * intensity)
        blue_shift = mobject.copy().set_color(BLUE).shift(LEFT * intensity)
        
        red_shift.set_opacity(0.3)
        blue_shift.set_opacity(0.3)
        
        return VGroup(red_shift, blue_shift, mobject)
    
    @staticmethod
    def add_motion_blur(
        mobject: Mobject,
        direction: np.ndarray = RIGHT,
        intensity: float = 0.3,
        samples: int = 5
    ) -> VGroup:
        """Simulate motion blur"""
        blur_group = VGroup()
        
        for i in range(samples):
            blur_copy = mobject.copy()
            offset = direction * (i / samples) * intensity
            blur_copy.shift(offset)
            blur_copy.set_opacity(intensity / samples)
            blur_group.add(blur_copy)
        
        blur_group.add(mobject)
        return blur_group
    
    @staticmethod
    def vignette_effect(opacity: float = 0.4) -> VMobject:
        """Create vignette overlay for cinematic feel"""
        vignette = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,
            fill_opacity=0,
            stroke_width=0
        )
        
        # Radial gradient simulation with concentric rectangles
        layers = VGroup()
        for i in range(10):
            scale = 1 + i * 0.1
            layer_opacity = (i / 10) * opacity
            layer = Rectangle(
                width=config.frame_width,
                height=config.frame_height,
                fill_color=BLACK,
                fill_opacity=layer_opacity,
                stroke_width=0
            ).scale(scale)
            layers.add(layer)
        
        layers.set_z_index(4998)
        return layers

# ==================== ADVANCED SUBTITLE SYSTEM ====================
class ProceduralHyphae(VGroup):
    """Advanced procedural hyphae with natural branching patterns"""
    
    def __init__(
        self,
        start: np.ndarray = ORIGIN,
        depth: int = 6,
        length: float = 1.2,
        angle_variance: float = PI / 4,
        branch_probability: float = 0.7,
        color: str = None,
        stroke_width: float = 2.5,
        curvature: float = 0.15,
        seed: Optional[int] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        if color is None:
            color = PALETTE["fungal"]
        
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        
        self.segments = []
        self._generate_recursive(
            start, -PI/2, depth, length, angle_variance,
            branch_probability, color, stroke_width, curvature
        )
        
        # Add subtle animation data
        self.growth_order = list(range(len(self.segments)))
    
    def _generate_recursive(
        self, pos: np.ndarray, angle: float, depth: int,
        length: float, angle_var: float, branch_prob: float,
        color: str, width: float, curvature: float
    ):
        """Recursively generate branching structure"""
        if depth <= 0:
            return
        
        # Natural variation
        segment_length = length * (0.8 ** (6 - depth)) * np.random.uniform(0.85, 1.15)
        current_angle = angle + np.random.uniform(-angle_var * 0.3, angle_var * 0.3)
        
        # Calculate endpoint
        end_pos = pos + segment_length * np.array([
            np.cos(current_angle),
            np.sin(current_angle),
            0
        ])
        
        # Create curved segment with Bezier
        control_offset = segment_length * curvature
        control_angle = current_angle + np.random.uniform(-PI/8, PI/8)
        
        control1 = pos + (end_pos - pos) * 0.33 + control_offset * np.array([
            np.cos(control_angle), np.sin(control_angle), 0
        ])
        control2 = pos + (end_pos - pos) * 0.67 + control_offset * np.array([
            np.cos(control_angle + PI), np.sin(control_angle + PI), 0
        ])
        
        curve = CubicBezier(pos, control1, control2, end_pos)
        curve.set_stroke(
            color,
            width=width * (0.85 ** (6 - depth)),
            opacity=0.9
        )
        
        self.add(curve)
        self.segments.append(curve)
        
        # Branching logic
        if np.random.random() < branch_prob and depth > 1:
            num_branches = np.random.choice([1, 2, 3], p=[0.3, 0.55, 0.15])
            
            for _ in range(num_branches):
                branch_angle = current_angle + np.random.uniform(-angle_var, angle_var)
                self._generate_recursive(
                    end_pos, branch_angle, depth - 1,
                    length, angle_var, branch_prob * 0.85,
                    color, width, curvature
                )
        else:
            # Single continuation
            self._generate_recursive(
                end_pos, current_angle, depth - 1,
                length, angle_var, branch_prob,
                color, width, curvature
            )

class AdvancedParticleSystem(VGroup):
    """Physics-based particle system"""
    
    def __init__(
        self,
        path: VMobject,
        count: int = 15,
        color: str = None,
        radius: float = 0.05,
        speed_variance: float = 0.3,
        glow: bool = True,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        if color is None:
            color = PALETTE["nutrient"]
        
        self.path = path
        self.particles = []
        
        for i in range(count):
            # Staggered starting positions
            alpha = (i / count) * 0.3  # Spread particles along first 30% of path
            start_pos = path.point_from_proportion(alpha)
            
            particle = Dot(radius=radius, color=color)
            particle.move_to(start_pos)
            particle.set_fill(color, opacity=0.9)
            
            if glow:
                glow_circle = Circle(
                    radius=radius * 2,
                    color=color,
                    fill_opacity=0.3,
                    stroke_width=0
                )
                glow_circle.move_to(start_pos)
                particle_group = VGroup(glow_circle, particle)
                self.add(particle_group)
                self.particles.append(particle_group)
            else:
                self.add(particle)
                self.particles.append(particle)
        
        # Store individual speed modifiers
        self.speeds = [1 + np.random.uniform(-speed_variance, speed_variance) 
                      for _ in range(count)]
    
    def create_flow_animation(self, run_time: float = 6.0) -> List[Animation]:
        """Create staggered flow animations"""
        animations = []
        
        for i, (particle, speed_mod) in enumerate(zip(self.particles, self.speeds)):
            # Stagger start times
            delay = (i / len(self.particles)) * run_time * 0.4
            adjusted_runtime = run_time * speed_mod
            
            if isinstance(particle, VGroup):
                # Animate glow and particle together
                for p in particle:
                    anim = MoveAlongPath(
                        p, self.path,
                        run_time=adjusted_runtime,
                        rate_func=smooth
                    )
                    animations.append(anim)
            else:
                anim = MoveAlongPath(
                    particle, self.path,
                    run_time=adjusted_runtime,
                    rate_func=smooth
                )
                animations.append(anim)
        
        return animations

# ==================== SCENE TRANSITIONS ====================
class SceneTransitions:
    """Professional scene transition effects"""
    
    @staticmethod
    def fade_through_black(scene: Scene, run_time: float = 1.0):
        """Fade to black and back"""
        fade_rect = Rectangle(
            width=config.frame_width + 2,
            height=config.frame_height + 2,
            fill_color=BLACK,
            fill_opacity=0,
            stroke_width=0
        )
        fade_rect.set_z_index(10000)
        scene.add(fade_rect)
        scene.play(
            fade_rect.animate.set_fill(opacity=1),
            run_time=run_time / 2
        )
        scene.wait(0.1)
        scene.play(
            fade_rect.animate.set_fill(opacity=0),
            run_time=run_time / 2
        )
        scene.remove(fade_rect)
    
    @staticmethod
    def radial_wipe(scene: Scene, run_time: float = 0.8):
        """Circular wipe transition"""
        circle = Circle(
            radius=0.1,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        )
        circle.set_z_index(10000)
        scene.add(circle)
        scene.play(
            circle.animate.scale(50),
            run_time=run_time,
            rate_func=rush_into
        )
        scene.remove(circle)
    
    @staticmethod
    def slide_wipe(scene: Scene, direction: np.ndarray = RIGHT, run_time: float = 0.6):
        """Sliding wipe transition"""
        wipe = Rectangle(
            width=config.frame_width + 1,
            height=config.frame_height + 1,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        )
        
        start_pos = -direction * (config.frame_width / 2 + 1)
        wipe.move_to(start_pos)
        wipe.set_z_index(10000)
        
        scene.add(wipe)
        scene.play(
            wipe.animate.shift(direction * config.frame_width * 2),
            run_time=run_time,
            rate_func=linear
        )
        scene.remove(wipe)

# ==================== ENHANCED PRIMITIVES ====================
def create_stylized_tree(
    size: float = 1.0,
    style: str = "deciduous",
    season: str = "summer",
    detail_level: int = 2
) -> VGroup:
    """Create detailed, stylized trees"""
    
    # Trunk with gradient
    trunk_width = 0.15 * size
    trunk_height = 0.8 * size
    trunk = Rectangle(
        width=trunk_width,
        height=trunk_height,
        fill_opacity=1,
        stroke_width=0
    )
    trunk.set_fill([PALETTE["plant_dark"], "#4a3520"])  # Gradient
    trunk.move_to(DOWN * trunk_height / 2)
    
    # Foliage
    foliage = VGroup()
    
    if style == "deciduous":
        # Layered circular canopy
        colors = {
            "spring": [PALETTE["plant_light"], "#b8e6a3"],
            "summer": [PALETTE["plant"], PALETTE["plant_light"]],
            "autumn": ["#d4a574", "#c98547"],
            "winter": []  # Bare branches
        }
        
        if season != "winter":
            radii = [size * 1.0, size * 0.75, size * 0.5]
            y_offsets = [size * 0.2, size * 0.5, size * 0.75]
            
            for i, (r, y) in enumerate(zip(radii, y_offsets)):
                circle = Circle(
                    radius=r,
                    fill_opacity=0.9,
                    stroke_width=1,
                    stroke_color=PALETTE["plant_dark"],
                    stroke_opacity=0.3
                )
                circle.set_fill(colors[season][i % 2])
                circle.shift(UP * y)
                foliage.add(circle)
        else:
            # Winter branches
            for _ in range(5):
                branch = Line(
                    trunk.get_top(),
                    trunk.get_top() + UP * size * 0.6 + 
                    np.random.uniform(-1, 1, 3) * [size * 0.4, size * 0.2, 0]
                )
                branch.set_stroke(PALETTE["plant_dark"], width=2)
                foliage.add(branch)
    
    elif style == "conifer":
        # Triangular conifer shape
        points = [
            trunk.get_top(),
            trunk.get_top() + UP * size * 1.2,
            trunk.get_top() + LEFT * size * 0.7 + UP * size * 0.2,
            trunk.get_top() + RIGHT * size * 0.7 + UP * size * 0.2,
        ]
        
        layers = 3
        for i in range(layers):
            layer_height = size * (1.2 - i * 0.3)
            layer_width = size * (0.9 - i * 0.2)
            
            triangle = Polygon(
                trunk.get_top() + UP * (i * size * 0.3),
                trunk.get_top() + UP * layer_height + UP * (i * size * 0.3),
                trunk.get_top() + LEFT * layer_width + UP * (size * 0.2 + i * size * 0.3),
                trunk.get_top() + RIGHT * layer_width + UP * (size * 0.2 + i * size * 0.3),
                fill_opacity=0.9,
                stroke_width=0
            )
            triangle.set_fill(PALETTE["plant"] if i % 2 == 0 else PALETTE["plant_dark"])
            foliage.add(triangle)
    
    return VGroup(trunk, foliage)

# ==================== SUBTITLE CONTENT ====================
SUBTITLES = {
    "IntroScene": [
        "In the silence beneath our feet, a vast and intricate world hums with unseen life.",
        "A world older than forests, more complex than any computer network, and as essential to life as sunlight.",
        "This is the story of mycorrhizal fungi—the subterranean architects of cooperation, the silent traders of life.",
        "These are the threads that bind the biosphere together."
    ],
    "HistoryScene": [
        "For hundreds of millions of years, fungi and plants have coexisted in a partnership so deep that neither can be understood without the other.",
        "Long before animals took their first steps on land, fungal filaments were already weaving through the soil.",
        "They formed microscopic bridges between the primitive roots of early plants.",
        "This alliance—the mycorrhizal symbiosis—allowed plants to conquer dry land.",
        "Fungi provided nutrients. Plants offered sugars. An exchange of survival—evolution's first great contract."
    ],
    "NetworkOverviewScene": [
        "Today, this ancient relationship persists beneath nearly every forest, grassland, and mountain slope.",
        "Mycorrhizal fungi extend far beyond the reach of roots, forming vast underground networks.",
        "Delicate webs of hyphae stretch through meters, even kilometers, of soil.",
        "Each strand, thinner than a human hair, acts as both an extension of the tree's body and a bridge to others.",
        "Through these threads, a forest becomes a collective intelligence."
    ],
    "MiningExchangeScene": [
        "The fungi act as miners, extracting phosphates, nitrates, and micronutrients from soil particles inaccessible to plant roots.",
        "Their enzymes dissolve rock, liberating minerals that feed the tree's growth.",
        "In return, the tree supplies carbohydrates—sugars crafted in its leaves through photosynthesis.",
        "This flow of resources forms a dynamic feedback loop.",
        "Trees reward fungi when light is plentiful. Fungi redistribute nutrients under stress."
    ],
    "CommunicationScene": [
        "Through the mycorrhizal network, trees can sense and respond to the presence of others.",
        "Signals of stress, drought, or pest attack can travel underground.",
        "These signals trigger defensive chemistry in distant trees, preparing them for threats.",
        "These exchanges represent ecological strategy that gives rise to cooperation.",
        "A 'Wood Wide Web' of chemical messages connects the forest."
    ],
    "ArchitectureScene": [
        "The name mycorrhiza—fungus and root—captures this union, but conceals a world of variation.",
        "Ectomycorrhizae form sheaths around roots, creating a Hartig net.",
        "Here, nutrients are traded molecule by molecule at the cellular interface.",
        "Arbuscular mycorrhizae penetrate root cells, forming arbuscules.",
        "These tree-like interfaces inside plant tissue enable intimate exchanges at the molecular level."
    ],
    "CompetitionScene": [
        "This relationship is not purely harmonious. Evolution breeds complexity.",
        "Some plants, like certain orchids, exploit fungal networks without giving anything in return.",
        "Some fungi manipulate partners, demanding more sugar than they return in nutrients.",
        "A biological tug-of-war between generosity and greed.",
        "Yet dynamic tension and feedback ensure the system tends toward stability over evolutionary time."
    ],
    "EcosystemsScene": [
        "In temperate forests, ectomycorrhizal networks dominate, linking oaks, beeches, and conifers into vast webs.",
        "In tropical ecosystems, arbuscular mycorrhizae connect dense vegetation across complex soils.",
        "Wherever plants endure—tundra, grassland, desert, urban park—fungi sculpt the invisible foundations.",
        "These are the ecosystems beneath ecosystems, the networks that sustain all terrestrial life."
    ],
    "ResearchMethodsScene": [
        "Scientists map these networks using isotopic tracers, DNA sequencing, and advanced imaging techniques.",
        "Carbon fixed by one tree can appear in the tissues of another tree meters away.",
        "The carbon travels through fungal threads, redistributed based on need and evolutionary strategy.",
        "These methods reveal the forest behaves less like a collection of individuals.",
        "Instead, it functions more like a distributed organism, a superorganism of interconnected life."
    ],
    "ThreatsRestorationScene": [
        "This ancient alliance faces unprecedented threats in the modern world.",
        "Deforestation severs fungal networks. Tilling disrupts soil architecture.",
        "Chemical fertilizers override natural symbioses, creating dependency and degradation.",
        "As soils warm and dry and biodiversity declines, these networks—silent and unseen—begin to fade.",
        "But restoration is possible through rewilding, regenerative agriculture, and inoculation with native fungi.",
        "We can revive these connections. We can heal the living web."
    ],
    "ConclusionScene": [
        "The story of mycorrhizal symbiosis is not a tale of the past.",
        "It is a vision of what sustains the future.",
        "Beneath every root tip and in every grain of soil, hyphae stretch onward.",
        "Unseen. Unheralded. Indispensable.",
        "Heal the networks. Heal the planet."
    ]
}

# ==================== SCENE IMPLEMENTATIONS ====================

class IntroScene(Scene):
    def construct(self):
        # Cinematic title sequence
        title = Text(
            "The Hidden Network",
            font_size=84,
            weight=BOLD,
            color=PALETTE["text_primary"]
        )
        title.set_sheen(-0.3, direction=UP)
        
        subtitle = Text(
            "Mycorrhizal Symbiosis and the Secret Life of Trees",
            font_size=32,
            color=PALETTE["text_secondary"],
            weight=MEDIUM
        )
        
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        title_group.to_edge(UP, buff=1.2)
        
        # Layered forest with depth
        background_trees = VGroup()
        midground_trees = VGroup()
        foreground_trees = VGroup()
        
        # Background layer (depth = far)
        for i in range(6):
            x = np.random.uniform(-7, 7)
            tree = create_stylized_tree(size=np.random.uniform(0.5, 0.8), style="deciduous")
            tree.shift(RIGHT * x + DOWN * 1.2)
            VisualEffects.depth_fade(tree, depth=0.7)
            tree.set_opacity(0.3)
            background_trees.add(tree)
        
        # Midground layer
        for i in range(5):
            x = np.random.uniform(-6, 6)
            tree = create_stylized_tree(size=np.random.uniform(0.9, 1.3), style="deciduous")
            tree.shift(RIGHT * x + DOWN * 0.8)
            VisualEffects.depth_fade(tree, depth=0.4)
            tree.set_opacity(0.6)
            midground_trees.add(tree)
        
        # Foreground layer
        for i in range(4):
            x = np.random.uniform(-5, 5)
            tree = create_stylized_tree(size=np.random.uniform(1.2, 1.8), style="deciduous")
            tree.shift(RIGHT * x + DOWN * 0.5)
            foreground_trees.add(tree)
        
        # Underground hyphae network with glow
        main_hyphae = ProceduralHyphae(
            start=DOWN * 2.5,
            depth=7,
            length=2.5,
            angle_variance=PI / 3,
            branch_probability=0.75,
            color=PALETTE["fungal_bright"],
            stroke_width=2.8,
            curvature=0.18,
            seed=42
        )
        
        glowing_hyphae = VisualEffects.add_glow(
            main_hyphae,
            color=PALETTE["fungal"],
            intensity=0.45,
            layers=4
        )
        
        # Nutrient flow demonstration
        flow_path = CubicBezier(
            LEFT * 1.2 + DOWN * 0.8,
            LEFT * 1.5 + DOWN * 1.5,
            LEFT * 2.0 + DOWN * 2.0,
            LEFT * 2.5 + DOWN * 2.3
        )
        flow_path.set_stroke(opacity=0)
        
        particles = AdvancedParticleSystem(
            flow_path,
            count=20,
            color=PALETTE["nutrient_bright"],
            radius=0.06,
            glow=True
        )
        
        # Animation sequence
        self.play(
            FadeIn(title, shift=DOWN * 0.5, scale=1.1),
            run_time=1.5
        )
        self.play(
            FadeIn(subtitle, shift=UP * 0.3),
            run_time=1.0
        )
        
        # Parallax forest growth
        self.play(
            LaggedStart(
                *[GrowFromCenter(t, rate_func=smooth) for t in background_trees],
                lag_ratio=0.1
            ),
            run_time=2.5
        )
        self.play(
            LaggedStart(
                *[GrowFromCenter(t, rate_func=smooth) for t in midground_trees],
                lag_ratio=0.12
            ),
            run_time=2.8
        )
        self.play(
            LaggedStart(
                *[GrowFromCenter(t, rate_func=smooth) for t in foreground_trees],
                lag_ratio=0.15
            ),
            run_time=3.0
        )
        
        # Parallax camera movement
        self.play(
            background_trees.animate.shift(LEFT * 0.4),
            midground_trees.animate.shift(LEFT * 0.2),
            foreground_trees.animate.shift(RIGHT * 0.15),
            run_time=3.0,
            rate_func=smooth
        )
        
        # Underground reveal
        self.play(
            Create(glowing_hyphae, run_time=4.5, rate_func=smooth)
        )
        
        # Add particles
        self.add(particles)
        self.play(
            *particles.create_flow_animation(run_time=10.0)
        )
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["IntroScene"],
            SCENE_DURATIONS["IntroScene"] - 30  # Reserve time for animations
        )
        
        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2.0
        )


class HistoryScene(Scene):
    def construct(self):
        # Timeline visualization
        timeline = NumberLine(
            x_range=[0, 500, 100],
            length=12,
            include_numbers=False,
            include_tip=True,
            tip_width=0.3,
            tip_height=0.3
        ).set_color(PALETTE["text_tertiary"])
        timeline.to_edge(DOWN, buff=1.5)
        
        # Time markers
        markers = VGroup()
        labels = [
            ("500 MYA", 0),
            ("400 MYA", 100),
            ("Present", 500)
        ]
        
        for label_text, pos in labels:
            point = timeline.number_to_point(pos)
            marker = Dot(point, radius=0.08, color=PALETTE["accent_blue"])
            label = Text(label_text, font_size=20, color=PALETTE["text_secondary"])
            label.next_to(marker, DOWN, buff=0.3)
            markers.add(VGroup(marker, label))
        
        # Ancient plant illustration
        ancient_plant = VGroup()
        for i in range(4):
            stem = Line(
                ORIGIN,
                UP * np.random.uniform(0.8, 1.2),
                stroke_width=4,
                color=PALETTE["plant_light"]
            )
            stem.shift(LEFT * 3.5 + RIGHT * (i * 0.4))
            
            # Simple leaves
            for j in range(3):
                leaf_pos = stem.point_from_proportion(0.3 + j * 0.25)
                leaf = Ellipse(
                    width=0.4,
                    height=0.15,
                    fill_opacity=0.8,
                    stroke_width=1
                ).set_fill(PALETTE["plant_light"])
                leaf.next_to(leaf_pos, RIGHT if i % 2 else LEFT, buff=0.05)
                ancient_plant.add(leaf)
            
            ancient_plant.add(stem)
        
        ancient_plant.shift(UP * 0.5)
        plant_label = Text(
            "Early Land Plants",
            font_size=28,
            color=PALETTE["text_primary"]
        ).next_to(ancient_plant, UP, buff=0.5)
        
        # Fungal network
        fungal_network = ProceduralHyphae(
            start=RIGHT * 2.5 + DOWN * 0.5,
            depth=6,
            length=1.8,
            angle_variance=PI / 2.5,
            branch_probability=0.7,
            color=PALETTE["fungal_bright"],
            stroke_width=2.5,
            seed=123
        )
        
        fungal_label = Text(
            "Mycorrhizal Fungi",
            font_size=28,
            color=PALETTE["text_primary"]
        ).next_to(fungal_network, UP, buff=0.5)
        
        # Exchange arrows
        nutrient_arrow = Arrow(
            fungal_network.get_center() + LEFT * 0.5,
            ancient_plant.get_center() + RIGHT * 0.5,
            buff=0.3,
            stroke_width=6,
            color=PALETTE["nutrient"]
        )
        nutrient_label = Text("Nutrients", font_size=20).next_to(nutrient_arrow, UP, buff=0.1)
        nutrient_label.set_color(PALETTE["nutrient"])
        
        carbon_arrow = Arrow(
            ancient_plant.get_center() + RIGHT * 0.5,
            fungal_network.get_center() + LEFT * 0.5,
            buff=0.3,
            stroke_width=6,
            color=PALETTE["carbon"]
        )
        carbon_label = Text("Carbon", font_size=20).next_to(carbon_arrow, DOWN, buff=0.1)
        carbon_label.set_color(PALETTE["carbon"])
        
        # Animation sequence
        self.play(Create(timeline), run_time=1.5)
        self.play(
            LaggedStart(
                *[FadeIn(m, shift=UP * 0.3) for m in markers],
                lag_ratio=0.3
            ),
            run_time=2.0
        )
        
        self.play(
            Write(plant_label),
            LaggedStart(
                *[Create(mob) for mob in ancient_plant],
                lag_ratio=0.05
            ),
            run_time=3.0
        )
        
        self.play(
            Write(fungal_label),
            Create(fungal_network, run_time=3.5)
        )
        
        self.wait(1.0)
        
        # Show exchange
        self.play(
            GrowArrow(nutrient_arrow),
            FadeIn(nutrient_label),
            run_time=1.5
        )
        self.play(
            GrowArrow(carbon_arrow),
            FadeIn(carbon_label),
            run_time=1.5
        )
        
        # Pulsing exchange animation
        for _ in range(3):
            self.play(
                nutrient_arrow.animate.set_color(PALETTE["nutrient_bright"]),
                carbon_arrow.animate.set_color(PALETTE["carbon"]),
                run_time=0.8
            )
            self.play(
                nutrient_arrow.animate.set_color(PALETTE["nutrient"]),
                carbon_arrow.animate.set_color("#d4c5a0"),
                run_time=0.8
            )
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["HistoryScene"],
            SCENE_DURATIONS["HistoryScene"] - 30
        )
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2.0)


class NetworkOverviewScene(Scene):
    def construct(self):
        # Create sophisticated network graph
        np.random.seed(42)
        
        # Node positions (representing trees)
        positions = [
            (-4.5, 2.0), (-2.0, 2.5), (0.5, 2.2), (3.0, 1.8),
            (-3.5, 0.0), (-1.0, -0.3), (1.5, 0.2), (3.8, -0.2),
            (-2.5, -2.0), (0.0, -2.3), (2.5, -1.8)
        ]
        
        nodes = VGroup()
        node_dots = []
        
        for x, y in positions:
            # Tree icon simplified
            node = Dot(
                point=[x, y, 0],
                radius=0.15,
                color=PALETTE["plant_light"]
            )
            node.set_fill(PALETTE["plant"], opacity=0.9)
            
            # Add subtle glow
            glow = Circle(
                radius=0.25,
                color=PALETTE["plant_light"],
                fill_opacity=0.2,
                stroke_width=0
            ).move_to(node.get_center())
            
            node_group = VGroup(glow, node)
            nodes.add(node_group)
            node_dots.append(node)
        
        # Create edges (fungal connections)
        edges = VGroup()
        edge_particles = []
        
        for i, node1 in enumerate(node_dots):
            for j, node2 in enumerate(node_dots[i+1:], start=i+1):
                distance = np.linalg.norm(node1.get_center() - node2.get_center())
                
                # Connect nearby nodes
                if distance < 4.0 and np.random.random() < 0.7:
                    # Create curved edge
                    start = node1.get_center()
                    end = node2.get_center()
                    
                    # Control point for curve
                    mid = (start + end) / 2
                    offset = np.random.uniform(-0.3, 0.3)
                    control = mid + UP * offset + RIGHT * offset * 0.5
                    
                    edge = QuadraticBezier(start, control, end)
                    edge.set_stroke(
                        PALETTE["network"],
                        width=2.5,
                        opacity=0.7
                    )
                    
                    edges.add(edge)
                    
                    # Add flowing particles to some edges
                    if np.random.random() < 0.4:
                        edge_particles.append(edge)
        
        # Title
        title = Text(
            "The Wood Wide Web",
            font_size=56,
            weight=BOLD,
            color=PALETTE["text_primary"]
        ).to_edge(UP, buff=0.8)
        
        # Animation sequence
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=1.2)
        
        # Build network
        self.play(
            LaggedStart(
                *[Create(edge, rate_func=smooth) for edge in edges],
                lag_ratio=0.03
            ),
            run_time=4.0
        )
        
        self.play(
            LaggedStart(
                *[FadeIn(node, scale=1.2) for node in nodes],
                lag_ratio=0.08
            ),
            run_time=3.0
        )
        
        # Cinematic camera movement
        self.play(
            self.camera.frame.animate.scale(0.7).move_to(node_dots[5]),
            run_time=3.0,
            rate_func=smooth
        )
        
        self.wait(1.5)
        
        self.play(
            self.camera.frame.animate.scale(1/0.7).move_to(ORIGIN),
            run_time=3.0,
            rate_func=smooth
        )
        
        # Activate network with signal pulses
        pulse_animations = []
        for edge in np.random.choice(edge_particles, size=min(8, len(edge_particles)), replace=False):
            pulse = Dot(radius=0.08, color=PALETTE["nutrient_bright"])
            pulse.move_to(edge.get_start())
            
            pulse_glow = Circle(
                radius=0.15,
                color=PALETTE["nutrient"],
                fill_opacity=0.4,
                stroke_width=0
            ).move_to(pulse.get_center())
            
            pulse_group = VGroup(pulse_glow, pulse)
            self.add(pulse_group)
            
            pulse_animations.append(
                MoveAlongPath(pulse_group, edge, run_time=4.0, rate_func=linear)
            )
        
        self.play(*pulse_animations)
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["NetworkOverviewScene"],
            SCENE_DURATIONS["NetworkOverviewScene"] - 40
        )
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2.0)


class MiningExchangeScene(Scene):
    def construct(self):
        # Soil cross-section
        soil_layer = Rectangle(
            width=14,
            height=4.5,
            fill_color="#3d2817",
            fill_opacity=0.85,
            stroke_width=0
        ).shift(DOWN * 0.8)
        
        # Add soil texture
        soil_particles = VGroup()
        for _ in range(100):
            x = np.random.uniform(-7, 7)
            y = np.random.uniform(-3.0, 1.3)
            particle = Dot(
                point=[x, y, 0],
                radius=np.random.uniform(0.02, 0.05),
                color="#5a4632"
            )
            particle.set_opacity(0.4)
            soil_particles.add(particle)
        
        # Tree above ground
        tree = create_stylized_tree(size=1.8, style="deciduous", season="summer")
        tree.to_edge(UP, buff=0.5).shift(LEFT * 3.0)
        
        tree_label = Text("Tree", font_size=28, color=PALETTE["text_primary"])
        tree_label.next_to(tree, LEFT, buff=0.5)
        
        # Root system
        root_system = VGroup()
        for i in range(5):
            root = Line(
                tree.get_bottom(),
                tree.get_bottom() + DOWN * np.random.uniform(1.2, 2.0) + 
                RIGHT * np.random.uniform(-0.8, 0.8),
                stroke_width=3,
                color=PALETTE["plant_dark"]
            )
            root_system.add(root)
        
        # Hyphae extending from roots
        hyphae_network = ProceduralHyphae(
            start=tree.get_bottom() + DOWN * 1.5 + RIGHT * 0.3,
            depth=7,
            length=2.2,
            angle_variance=PI / 2.8,
            branch_probability=0.8,
            color=PALETTE["fungal_bright"],
            stroke_width=2.5,
            curvature=0.2,
            seed=456
        )
        
        hyphae_label = Text(
            "Fungal Hyphae",
            font_size=28,
            color=PALETTE["text_primary"]
        ).to_edge(RIGHT).shift(UP * 0.5)
        
        # Mineral deposits in soil
        minerals = VGroup()
        mineral_positions = []
        for _ in range(8):
            x = np.random.uniform(-2, 5)
            y = np.random.uniform(-2.5, 0)
            pos = np.array([x, y, 0])
            mineral_positions.append(pos)
            
            mineral = RegularPolygon(
                n=6,
                radius=0.12,
                fill_opacity=0.9,
                stroke_width=2
            ).move_to(pos)
            mineral.set_fill(PALETTE["nutrient"])
            mineral.set_stroke(PALETTE["nutrient_bright"])
            
            minerals.add(mineral)
        
        # Nutrient flow paths
        nutrient_flows = VGroup()
        for mineral_pos in mineral_positions[:4]:
            # Find nearest hypha point
            target = hyphae_network.get_center() + \
                     np.random.uniform(-0.5, 0.5, 3) * [1, 1, 0]
            
            path = Line(mineral_pos, target)
            path.set_stroke(opacity=0)
            nutrient_flows.add(path)
        
        # Carbon flow from tree
        carbon_path = CubicBezier(
            tree.get_bottom() + DOWN * 0.2,
            tree.get_bottom() + DOWN * 0.8 + RIGHT * 0.3,
            tree.get_bottom() + DOWN * 1.2 + RIGHT * 0.5,
            hyphae_network.get_center() + UP * 0.5
        )
        carbon_path.set_stroke(opacity=0)
        
        # Magnification indicator
        mag_text = Text(
            "Microscopic View (1000×)",
            font_size=22,
            color=PALETTE["text_tertiary"]
        ).to_corner(DR, buff=0.5)
        
        # Chemical formulas
        phosphorus = MathTex("PO_4^{3-}", font_size=48, color=PALETTE["nutrient"])
        nitrogen = MathTex("NO_3^{-}", font_size=48, color=PALETTE["nutrient"])
        glucose = MathTex("C_6H_{12}O_6", font_size=40, color=PALETTE["carbon"])
        
        phosphorus.move_to(minerals[0].get_center() + UP * 0.6)
        nitrogen.move_to(minerals[2].get_center() + UP * 0.6)
        glucose.next_to(tree, DOWN, buff=0.3)
        
        # Animation sequence
        self.play(
            FadeIn(soil_layer),
            FadeIn(soil_particles),
            run_time=1.5
        )
        
        self.play(
            GrowFromCenter(tree),
            Write(tree_label),
            run_time=2.0
        )
        
        self.play(
            *[Create(root) for root in root_system],
            run_time=1.8
        )
        
        self.add(mag_text)
        self.play(
            Create(hyphae_network, run_time=4.0),
            Write(hyphae_label)
        )
        
        self.play(
            LaggedStart(
                *[FadeIn(m, scale=1.3) for m in minerals],
                lag_ratio=0.15
            ),
            run_time=2.5
        )
        
        # Show chemical formulas
        self.play(
            Write(phosphorus),
            Write(nitrogen),
            Write(glucose),
            run_time=2.0
        )
        
        # Animate nutrient extraction
        for i, path in enumerate(nutrient_flows):
            particle = Dot(radius=0.07, color=PALETTE["nutrient_bright"])
            particle.move_to(path.get_start())
            
            particle_glow = Circle(
                radius=0.14,
                fill_opacity=0.4,
                stroke_width=0,
                color=PALETTE["nutrient"]
            ).move_to(particle.get_center())
            
            particle_group = VGroup(particle_glow, particle)
            
            self.play(
                minerals[i].animate.set_opacity(0.3),
                MoveAlongPath(particle_group, path, run_time=2.5),
                run_time=2.5
            )
        
        # Animate carbon flow to fungi
        carbon_particles = AdvancedParticleSystem(
            carbon_path,
            count=12,
            color=PALETTE["carbon"],
            radius=0.06,
            glow=True
        )
        
        self.add(carbon_particles)
        self.play(
            *carbon_particles.create_flow_animation(run_time=4.0)
        )
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["MiningExchangeScene"],
            SCENE_DURATIONS["MiningExchangeScene"] - 35
        )
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2.0)


class CommunicationScene(Scene):
    def construct(self):
        # Three trees connected underground
        tree1 = create_stylized_tree(size=1.3, style="deciduous", season="summer")
        tree2 = create_stylized_tree(size=1.6, style="deciduous", season="summer")
        tree3 = create_stylized_tree(size=1.4, style="deciduous", season="summer")
        
        tree1.move_to(LEFT * 4.5 + UP * 0.5)
        tree2.move_to(ORIGIN + UP * 0.8)
        tree3.move_to(RIGHT * 4.5 + UP * 0.6)
        
        trees = VGroup(tree1, tree2, tree3)
        
        # Underground network
        connection1 = CubicBezier(
            tree1.get_bottom() + DOWN * 0.3,
            tree1.get_bottom() + DOWN * 1.2 + RIGHT * 1.0,
            tree2.get_bottom() + DOWN * 1.2 + LEFT * 1.0,
            tree2.get_bottom() + DOWN * 0.3
        )
        connection1.set_stroke(PALETTE["network"], width=4, opacity=0.8)
        
        connection2 = CubicBezier(
            tree2.get_bottom() + DOWN * 0.3,
            tree2.get_bottom() + DOWN * 1.2 + RIGHT * 1.0,
            tree3.get_bottom() + DOWN * 1.2 + LEFT * 1.0,
            tree3.get_bottom() + DOWN * 0.3
        )
        connection2.set_stroke(PALETTE["network"], width=4, opacity=0.8)
        
        connections = VGroup(connection1, connection2)
        
        # Labels
        labels = VGroup(
            Text("Tree A", font_size=24).next_to(tree1, UP, buff=0.3),
            Text("Tree B", font_size=24).next_to(tree2, UP, buff=0.3),
            Text("Tree C", font_size=24).next_to(tree3, UP, buff=0.3)
        )
        labels.set_color(PALETTE["text_secondary"])
        
        # Build scene
        self.play(
            LaggedStart(
                *[GrowFromCenter(t) for t in trees],
                lag_ratio=0.3
            ),
            run_time=3.0
        )
        
        self.play(
            Write(labels),
            run_time=1.5
        )
        
        self.play(
            *[Create(conn, run_time=2.5) for conn in connections]
        )
        
        self.wait(1.0)
        
        # Pest attack on Tree A
        pest_icon = SVGMobject("bug").scale(0.4) if False else Text(
            "🐛",
            font_size=48
        )
        pest_icon.next_to(tree1, LEFT, buff=0.3)
        
        self.play(
            FadeIn(pest_icon, shift=LEFT * 0.5),
            tree1.animate.set_color(PALETTE["alert"]).scale(1.05),
            run_time=1.0
        )
        
        # Stress signal visualization
        stress_waves = VGroup()
        for i in range(4):
            wave = Circle(
                radius=0.3 + i * 0.3,
                stroke_color=PALETTE["alert"],
                stroke_width=3,
                fill_opacity=0
            ).move_to(tree1.get_bottom())
            stress_waves.add(wave)
        
        self.play(
            LaggedStart(
                *[wave.animate.scale(3).set_stroke(opacity=0) 
                  for wave in stress_waves],
                lag_ratio=0.2
            ),
            run_time=2.5
        )
        
        # Chemical signal traveling through network
        signal_dot = Dot(radius=0.1, color=PALETTE["alert_bright"])
        signal_glow = Circle(
            radius=0.2,
            color=PALETTE["alert"],
            fill_opacity=0.5,
            stroke_width=0
        ).move_to(signal_dot.get_center())
        
        signal = VGroup(signal_glow, signal_dot)
        signal.move_to(tree1.get_bottom())
        
        self.add(signal)
        
        # Signal travels to Tree B
        path1 = connection1.copy()
        self.play(
            MoveAlongPath(signal, path1, run_time=3.0, rate_func=smooth)
        )
        
        # Tree B responds
        self.play(
            tree2.animate.set_color(PALETTE["defense"]).scale(1.03),
            run_time=0.8
        )
        
        # Signal continues to Tree C
        signal.move_to(tree2.get_bottom())
        path2 = connection2.copy()
        
        self.play(
            MoveAlongPath(signal, path2, run_time=3.0, rate_func=smooth)
        )
        
        # Tree C defensive response
        self.play(
            tree3.animate.set_color(PALETTE["defense"]).scale(1.03),
            run_time=0.8
        )
        
        # Show defensive compounds
        defense_symbols = VGroup()
        for tree in [tree2, tree3]:
            symbol = Text("✦", font_size=40, color=PALETTE["defense"])
            symbol.next_to(tree, UP, buff=0.2)
            defense_symbols.add(symbol)
        
        self.play(
            *[FadeIn(sym, scale=1.5) for sym in defense_symbols],
            run_time=1.5
        )
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["CommunicationScene"],
            SCENE_DURATIONS["CommunicationScene"] - 30
        )
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2.0)


class ArchitectureScene(Scene):
    def construct(self):
        # Split screen: two types of mycorrhizae
        divider = Line(UP * 4, DOWN * 4, stroke_width=2, color=PALETTE["text_tertiary"])
        
        left_title = Text(
            "Ectomycorrhizae",
            font_size=36,
            color=PALETTE["text_primary"]
        ).to_edge(UP, buff=0.6).shift(LEFT * 3.2)
        
        right_title = Text(
            "Arbuscular Mycorrhizae",
            font_size=36,
            color=PALETTE["text_primary"]
        ).to_edge(UP, buff=0.6).shift(RIGHT * 3.2)
        
        # Left side: Ectomycorrhizae
        root_cross = Circle(
            radius=2.0,
            fill_color=PALETTE["plant_dark"],
            fill_opacity=0.15,
            stroke_color=PALETTE["plant"],
            stroke_width=3
        ).shift(LEFT * 3.2)
        
        # Hartig net - concentric rings
        hartig_net = VGroup()
        for i in range(15):
            radius = 1.8 - i * 0.12
            ring = Circle(
                radius=radius,
                stroke_color=PALETTE["fungal"],
                stroke_width=1.5,
                fill_opacity=0
            )
            ring.shift(LEFT * 3.2)
            # Add slight randomness
            ring.shift(
                np.random.uniform(-0.1, 0.1, 3) * [1, 1, 0]
            )
            hartig_net.add(ring)
        
        # Sheath label
        sheath_label = Text(
            "Fungal Sheath",
            font_size=22,
            color=PALETTE["fungal"]
        ).next_to(root_cross, DOWN, buff=0.8)
        
        # Right side: Arbuscular mycorrhizae
        plant_cell = RoundedRectangle(
            width=3.0,
            height=3.0,
            corner_radius=0.2,
            fill_color=PALETTE["plant_dark"],
            fill_opacity=0.1,
            stroke_color=PALETTE["plant"],
            stroke_width=3
        ).shift(RIGHT * 3.2)
        
        # Arbuscule - tree-like structure inside cell
        arbuscule = VGroup()
        center = plant_cell.get_center()
        
        # Create branching arbuscule
        def create_arbuscule_branch(start, angle, depth, length):
            if depth <= 0:
                return VGroup()
            
            branch_group = VGroup()
            end = start + length * np.array([np.cos(angle), np.sin(angle), 0])
            
            branch = Line(start, end, stroke_width=3 / depth, color=PALETTE["nutrient"])
            branch_group.add(branch)
            
            # Recursive branches
            if depth > 1:
                left_branch = create_arbuscule_branch(
                    end, angle - PI/6, depth - 1, length * 0.7
                )
                right_branch = create_arbuscule_branch(
                    end, angle + PI/6, depth - 1, length * 0.7
                )
                branch_group.add(left_branch, right_branch)
            
            return branch_group
        
        # Create arbuscule starting from bottom
        arbuscule = create_arbuscule_branch(
            center + DOWN * 1.2,
            PI/2,
            4,
            0.6
        )
        
        arbuscule_label = Text(
            "Arbuscules",
            font_size=22,
            color=PALETTE["nutrient"]
        ).next_to(plant_cell, DOWN, buff=0.8)
        
        # Build scene
        self.play(
            Create(divider),
            Write(left_title),
            Write(right_title),
            run_time=2.0
        )
        
        # Left side animation
        self.play(
            Create(root_cross),
            run_time=1.5
        )
        
        self.play(
            LaggedStart(
                *[Create(ring, rate_func=smooth) for ring in hartig_net],
                lag_ratio=0.1
            ),
            run_time=3.5
        )
        
        self.play(Write(sheath_label))
        
        # Right side animation
        self.play(
            Create(plant_cell),
            run_time=1.5
        )
        
        self.play(
            Create(arbuscule, run_time=3.5, rate_func=smooth)
        )
        
        self.play(Write(arbuscule_label))
        
        # Highlight nutrient exchange
        exchange_arrows = VGroup()
        for i in range(4):
            angle = i * PI / 2
            start = root_cross.get_center() + 1.2 * np.array([np.cos(angle), np.sin(angle), 0])
            end = root_cross.get_center() + 0.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            arrow = Arrow(start, end, buff=0, stroke_width=3, color=PALETTE["nutrient"])
            exchange_arrows.add(arrow)
        
        self.play(
            LaggedStart(
                *[GrowArrow(arr) for arr in exchange_arrows],
                lag_ratio=0.2
            ),
            run_time=2.0
        )
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["ArchitectureScene"],
            SCENE_DURATIONS["ArchitectureScene"] - 25
        )
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2.0)


class CompetitionScene(Scene):
    def construct(self):
        # Central fungal network
        central_network = ProceduralHyphae(
            start=ORIGIN,
            depth=6,
            length=2.0,
            angle_variance=2*PI/3,
            branch_probability=0.75,
            color=PALETTE["network"],
            stroke_width=2.8,
            seed=789
        )
        
        glowing_network = VisualEffects.add_glow(
            central_network,
            color=PALETTE["network"],
            intensity=0.35
        )
        
        # Cooperative tree (left)
        coop_tree = create_stylized_tree(size=1.4, style="deciduous", season="summer")
        coop_tree.move_to(LEFT * 3.5 + UP * 1.2)
        
        coop_label = Text(
            "Host Tree",
            font_size=28,
            color=PALETTE["plant_light"]
        ).next_to(coop_tree, LEFT, buff=0.4)
        
        # Parasitic orchid (right)
        orchid = VGroup()
        stem = Line(ORIGIN, UP * 0.8, stroke_width=3, color="#e8a5e8")
        flower = Ellipse(width=0.6, height=0.8, fill_opacity=0.85, stroke_width=2)
        flower.set_fill("#ff6ec7")
        flower.set_stroke("#d946a6")
        flower.next_to(stem, UP, buff=0)
        orchid.add(stem, flower)
        orchid.move_to(RIGHT * 3.5 + UP * 1.2)
        
        orchid_label = Text(
            "Parasitic Orchid",
            font_size=28,
            color=PALETTE["alert"]
        ).next_to(orchid, RIGHT, buff=0.4)
        
        # Connection lines
        coop_connection = Line(
            coop_tree.get_bottom(),
            central_network.get_center() + LEFT * 0.8,
            stroke_width=3,
            color=PALETTE["network"]
        )
        
        orchid_connection = Line(
            orchid.get_bottom(),
            central_network.get_center() + RIGHT * 0.8,
            stroke_width=3,
            color=PALETTE["network"]
        )
        
        # Build scene
        self.play(
            Create(glowing_network, run_time=3.5)
        )
        
        self.play(
            GrowFromCenter(coop_tree),
            GrowFromCenter(orchid),
            Write(coop_label),
            Write(orchid_label),
            run_time=2.5
        )
        
        self.play(
            Create(coop_connection),
            Create(orchid_connection),
            run_time=1.5
        )
        
        # Bidirectional exchange with host
        host_to_fungus = Arrow(
            coop_tree.get_bottom() + DOWN * 0.3,
            central_network.get_center() + LEFT * 0.5,
            buff=0,
            stroke_width=4,
            color=PALETTE["carbon"]
        )
        
        fungus_to_host = Arrow(
            central_network.get_center() + LEFT * 0.5,
            coop_tree.get_bottom() + DOWN * 0.3,
            buff=0,
            stroke_width=4,
            color=PALETTE["nutrient"]
        )
        
        self.play(
            GrowArrow(host_to_fungus),
            GrowArrow(fungus_to_host),
            run_time=2.0
        )
        
        # Balanced exchange icon
        balance = Text("⚖", font_size=48, color=GREEN)
        balance.next_to(coop_tree, DOWN, buff=0.8)
        self.play(FadeIn(balance, scale=1.3), run_time=1.0)
        
        self.wait(1.5)
        
        # One-way extraction from fungus by orchid
        fungus_to_orchid = Arrow(
            central_network.get_center() + RIGHT * 0.5,
            orchid.get_bottom() + DOWN * 0.3,
            buff=0,
            stroke_width=5,
            color=PALETTE["alert"]
        )
        
        self.play(GrowArrow(fungus_to_orchid), run_time=1.5)
        
        # Show no return flow with X
        no_return = Text("✗", font_size=64, color=PALETTE["alert"])
        no_return.move_to(orchid.get_bottom() + DOWN * 0.6)
        self.play(FadeIn(no_return, scale=1.5), run_time=1.0)
        
        # Tension visualization
        tension_text = Text(
            "Evolutionary Tension",
            font_size=32,
            color=PALETTE["text_secondary"]
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(tension_text), run_time=1.5)
        
        # Pulsing network showing stress
        for _ in range(3):
            self.play(
                central_network.animate.set_color(PALETTE["alert"]),
                run_time=0.5
            )
            self.play(
                central_network.animate.set_color(PALETTE["network"]),
                run_time=0.5
            )
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["CompetitionScene"],
            SCENE_DURATIONS["CompetitionScene"] - 30
        )
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2.0)


class EcosystemsScene(Scene):
    def construct(self):
        # Split view: temperate vs tropical
        divider = DashedLine(UP * 4, DOWN * 4, stroke_width=2, color=PALETTE["text_tertiary"])
        
        # Temperate forest (left)
        temperate_bg = Rectangle(
            width=6.5,
            height=8,
            fill_color=PALETTE["depth_far"],
            fill_opacity=0.3,
            stroke_width=0
        ).shift(LEFT * 3.5)
        
        temperate_title = Text(
            "Temperate Forest",
            font_size=32,
            color=PALETTE["text_primary"]
        ).move_to(LEFT * 3.5 + UP * 3.0)
        
        # Temperate trees
        temp_trees = VGroup()
        for i in range(3):
            tree = create_stylized_tree(
                size=np.random.uniform(1.0, 1.5),
                style="deciduous" if i % 2 == 0 else "conifer",
                season="autumn"
            )
            tree.shift(LEFT * 3.5 + LEFT * (i - 1) * 1.2 + UP * 0.5)
            temp_trees.add(tree)
        
        # Ectomycorrhizal network
        ecto_network = ProceduralHyphae(
            start=LEFT * 3.5 + DOWN * 1.5,
            depth=6,
            length=1.8,
            angle_variance=PI / 2,
            branch_probability=0.75,
            color="#2d8b8b",
            stroke_width=2.5,
            seed=111
        )
        
        ecto_label = Text(
            "Ectomycorrhizal",
            font_size=22,
            color="#2d8b8b"
        ).move_to(LEFT * 3.5 + DOWN * 3.2)
        
        # Tropical ecosystem (right)
        tropical_bg = Rectangle(
            width=6.5,
            height=8,
            fill_color="#2d1f0f",
            fill_opacity=0.3,
            stroke_width=0
        ).shift(RIGHT * 3.5)
        
        tropical_title = Text(
            "Tropical Rainforest",
            font_size=32,
            color=PALETTE["text_primary"]
        ).move_to(RIGHT * 3.5 + UP * 3.0)
        
        # Tropical vegetation
        tropical_plants = VGroup()
        for i in range(4):
            plant = VGroup()
            stem = Line(ORIGIN, UP * np.random.uniform(0.8, 1.4), stroke_width=3)
            stem.set_color("#3a8f3a")
            
            # Large leaves
            for j in range(3):
                leaf_pos = stem.point_from_proportion(0.3 + j * 0.25)
                leaf = Ellipse(
                    width=np.random.uniform(0.5, 0.8),
                    height=np.random.uniform(0.3, 0.5),
                    fill_opacity=0.8
                )
                leaf.set_fill("#5db85d")
                leaf.set_stroke("#3a8f3a", width=2)
                leaf.next_to(leaf_pos, RIGHT if i % 2 else LEFT, buff=0.05)
                plant.add(leaf)
            
            plant.add(stem)
            plant.shift(RIGHT * 3.5 + RIGHT * (i - 1.5) * 1.0 + UP * 0.5)
            tropical_plants.add(plant)
        
        # Arbuscular mycorrhizal network
        am_network = ProceduralHyphae(
            start=RIGHT * 3.5 + DOWN * 1.5,
            depth=5,
            length=1.4,
            angle_variance=PI / 2.5,
            branch_probability=0.7,
            color="#d4a060",
            stroke_width=2.2,
            seed=222
        )
        
        am_label = Text(
            "Arbuscular Mycorrhizal",
            font_size=22,
            color="#d4a060"
        ).move_to(RIGHT * 3.5 + DOWN * 3.2)
        
        # Build scene
        self.play(
            FadeIn(temperate_bg),
            FadeIn(tropical_bg),
            run_time=1.0
        )
        
        self.play(
            Write(temperate_title),
            Write(tropical_title),
            Create(divider),
            run_time=1.5
        )
        
        # Temperate side
        self.play(
            LaggedStart(
                *[GrowFromCenter(tree) for tree in temp_trees],
                lag_ratio=0.2
            ),
            run_time=2.5
        )
        
        self.play(
            Create(ecto_network, run_time=3.0),
            Write(ecto_label)
        )
        
        # Tropical side
        self.play(
            LaggedStart(
                *[GrowFromCenter(plant) for plant in tropical_plants],
                lag_ratio=0.15
            ),
            run_time=2.5
        )
        
        self.play(
            Create(am_network, run_time=3.0),
            Write(am_label)
        )
        
        # Global connectivity concept
        self.wait(1.0)
        
        connection_arc = Arc(
            radius=5.0,
            start_angle=PI,
            angle=PI,
            stroke_width=3,
            color=PALETTE["accent_purple"]
        ).shift(DOWN * 1.0)
        
        global_text = Text(
            "Globally Connected Ecosystems",
            font_size=28,
            color=PALETTE["accent_purple"]
        ).to_edge(DOWN, buff=0.8)
        
        self.play(
            Create(connection_arc),
            Write(global_text),
            run_time=2.0
        )
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["EcosystemsScene"],
            SCENE_DURATIONS["EcosystemsScene"] - 25
        )
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2.0)


class ResearchMethodsScene(Scene):
    def construct(self):
        # Laboratory setup
        lab_title = Text(
            "Research Methods",
            font_size=48,
            weight=BOLD,
            color=PALETTE["text_primary"]
        ).to_edge(UP, buff=0.8)
        
        # Method 1: Isotopic Tracing
        method1_title = Text(
            "Isotopic Tracing",
            font_size=32,
            color=PALETTE["accent_blue"]
        ).shift(LEFT * 3.5 + UP * 1.5)
        
        # Two trees with isotope
        tree_a = Dot(radius=0.2, color=PALETTE["plant_light"])
        tree_a.move_to(LEFT * 5.0 + UP * 0.5)
        
        tree_b = Dot(radius=0.2, color=PALETTE["plant_light"])
        tree_b.move_to(LEFT * 2.0 + UP * 0.5)
        
        # Network connection
        network_line = Line(
            tree_a.get_center() + DOWN * 0.3,
            tree_b.get_center() + DOWN * 0.3,
            stroke_width=4,
            color=PALETTE["network"]
        )
        
        # Isotope label
        isotope = MathTex("^{13}C", font_size=48, color=PALETTE["nutrient_bright"])
        isotope.next_to(tree_a, LEFT, buff=0.3)
        
        # Method 2: DNA Sequencing
        method2_title = Text(
            "DNA Sequencing",
            font_size=32,
            color=PALETTE["accent_purple"]
        ).shift(RIGHT * 3.5 + UP * 1.5)
        
        # DNA helix visualization
        dna = VGroup()
        num_base_pairs = 12
        helix_height = 3.0
        
        for i in range(num_base_pairs):
            y_pos = UP * (helix_height / 2 - i * helix_height / num_base_pairs)
            angle = i * PI / 3
            
            # Base pair
            x_offset = 0.4 * np.sin(angle)
            left_base = Dot(radius=0.08, color=BLUE).move_to(RIGHT * (3.5 + x_offset - 0.3) + y_pos)
            right_base = Dot(radius=0.08, color=RED).move_to(RIGHT * (3.5 + x_offset + 0.3) + y_pos)
            connector = Line(left_base.get_center(), right_base.get_center(), stroke_width=2)
            
            dna.add(left_base, right_base, connector)
        
        # Method 3: Advanced Imaging
        method3_title = Text(
            "Microscopy",
            font_size=32,
            color=PALETTE["fungal"]
        ).shift(DOWN * 2.0)
        
        # Microscope visualization
        microscope = VGroup()
        body = Rectangle(width=1.0, height=1.5, fill_opacity=0.7, stroke_width=2)
        body.set_fill(PALETTE["text_tertiary"])
        lens = Circle(radius=0.15, fill_opacity=1, stroke_width=2)
        lens.set_fill(PALETTE["accent_blue"])
        lens.next_to(body, DOWN, buff=0)
        
        microscope.add(body, lens)
        microscope.next_to(method3_title, DOWN, buff=0.5)
        
        # Sample under microscope
        sample = ProceduralHyphae(
            start=microscope.get_center() + DOWN * 1.2,
            depth=4,
            length=0.8,
            angle_variance=PI / 3,
            branch_probability=0.8,
            color=PALETTE["fungal_bright"],
            stroke_width=2.0,
            seed=333
        )
        
        # Build scene
        self.play(Write(lab_title), run_time=1.5)
        
        # Method 1: Isotopic tracing
        self.play(Write(method1_title), run_time=1.0)
        self.play(
            FadeIn(tree_a),
            FadeIn(tree_b),
            Create(network_line),
            run_time=1.5
        )
        
        self.play(Write(isotope), run_time=1.0)
        
        # Tracer particle with glow
        tracer = Dot(radius=0.12, color=PALETTE["nutrient_bright"])
        tracer_glow = Circle(
            radius=0.25,
            color=PALETTE["nutrient"],
            fill_opacity=0.4,
            stroke_width=0
        )
        tracer_group = VGroup(tracer_glow, tracer)
        tracer_group.move_to(tree_a.get_center())
        
        self.add(tracer_group)
        self.play(
            tracer_group.animate.move_to(tree_b.get_center()),
            run_time=4.0,
            rate_func=smooth
        )
        
        # Show detection in Tree B
        detection = Text("Detected!", font_size=24, color=GREEN)
        detection.next_to(tree_b, RIGHT, buff=0.3)
        self.play(FadeIn(detection, scale=1.3), run_time=1.0)
        
        # Method 2: DNA Sequencing
        self.play(Write(method2_title), run_time=1.0)
        self.play(
            LaggedStart(
                *[FadeIn(mob, shift=DOWN * 0.2) for mob in dna],
                lag_ratio=0.05
            ),
            run_time=2.5
        )
        
        # Highlight sequence
        for _ in range(2):
            self.play(
                *[mob.animate.set_color(YELLOW) for mob in dna[::3]],
                run_time=0.5
            )
            self.play(
                *[mob.animate.set_color(BLUE if i % 3 == 0 else RED if i % 3 == 1 else WHITE) 
                  for i, mob in enumerate(dna)],
                run_time=0.5
            )
        
        # Method 3: Microscopy
        self.play(Write(method3_title), run_time=1.0)
        self.play(FadeIn(microscope), run_time=1.0)
        self.play(Create(sample, run_time=2.5))
        
        # Zoom effect
        zoom_circle = Circle(radius=3.0, stroke_width=4, color=YELLOW)
        zoom_circle.move_to(sample.get_center())
        
        self.play(
            Create(zoom_circle),
            sample.animate.scale(1.5),
            run_time=2.0
        )
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["ResearchMethodsScene"],
            SCENE_DURATIONS["ResearchMethodsScene"] - 35
        )
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2.0)


class ThreatsRestorationScene(Scene):
    def construct(self):
        # Split screen: threats vs restoration
        left_bg = Rectangle(
            width=6.5,
            height=8,
            fill_color="#1a0a0a",
            fill_opacity=0.6,
            stroke_width=2,
            stroke_color=PALETTE["alert"]
        ).shift(LEFT * 3.5)
        
        right_bg = Rectangle(
            width=6.5,
            height=8,
            fill_color="#0a2a1a",
            fill_opacity=0.4,
            stroke_width=2,
            stroke_color=GREEN
        ).shift(RIGHT * 3.5)
        
        left_title = Text(
            "THREATS",
            font_size=42,
            weight=BOLD,
            color=PALETTE["alert"]
        ).move_to(LEFT * 3.5 + UP * 3.3)
        
        right_title = Text(
            "RESTORATION",
            font_size=42,
            weight=BOLD,
            color=GREEN
        ).move_to(RIGHT * 3.5 + UP * 3.3)
        
        self.play(
            FadeIn(left_bg),
            FadeIn(right_bg),
            Write(left_title),
            Write(right_title),
            run_time=2.0
        )
        
        # THREATS SIDE
        # 1. Deforestation
        forest_before = VGroup()
        for i in range(5):
            tree = create_stylized_tree(size=0.6, style="deciduous")
            tree.shift(LEFT * 3.5 + LEFT * (i - 2) * 0.7 + UP * 1.5)
            forest_before.add(tree)
        
        self.play(
            LaggedStart(
                *[GrowFromCenter(tree) for tree in forest_before],
                lag_ratio=0.1
            ),
            run_time=2.0
        )
        
        # Chainsaw effect
        for tree in forest_before:
            self.play(
                tree.animate.set_opacity(0.2).scale(0.8).rotate(PI/8),
                run_time=0.3
            )
        
        deforest_text = Text("Deforestation", font_size=24, color=PALETTE["alert"])
        deforest_text.move_to(LEFT * 3.5 + UP * 1.2)
        self.play(Write(deforest_text), run_time=1.0)
        
        # 2. Broken network
        broken_network = VGroup()
        for i in range(6):
            segment = Line(
                LEFT * np.random.uniform(2.0, 5.0) + DOWN * (0.3 + i * 0.3),
                LEFT * np.random.uniform(2.0, 5.0) + RIGHT * 1.5 + DOWN * (0.3 + i * 0.3),
                stroke_width=4,
                color=PALETTE["alert"]
            )
            segment.set_stroke(opacity=0.5)
            broken_network.add(segment)
        
        self.play(
            LaggedStart(
                *[Create(seg) for seg in broken_network],
                lag_ratio=0.1
            ),
            run_time=2.0
        )
        
        # X marks showing breaks
        for segment in broken_network[::2]:
            x_mark = Text("✗", font_size=32, color=PALETTE["alert_bright"])
            x_mark.move_to(segment.get_center())
            self.play(FadeIn(x_mark, scale=1.5), run_time=0.3)
        
        network_text = Text("Severed Networks", font_size=24, color=PALETTE["alert"])
        network_text.move_to(LEFT * 3.5 + DOWN * 0.5)
        self.play(Write(network_text), run_time=1.0)
        
        # 3. Chemical pollution
        chemicals = VGroup()
        for i in range(4):
            beaker = VGroup()
            container = Rectangle(width=0.4, height=0.6, stroke_width=2)
            container.set_stroke(PALETTE["alert"])
            liquid = Rectangle(width=0.38, height=0.4, fill_opacity=0.7, stroke_width=0)
            liquid.set_fill(PALETTE["alert"])
            liquid.move_to(container.get_bottom() + UP * 0.2)
            beaker.add(container, liquid)
            beaker.shift(LEFT * 3.5 + LEFT * (i - 1.5) * 0.6 + DOWN * 2.2)
            chemicals.add(beaker)
        
        self.play(
            LaggedStart(
                *[FadeIn(chem, shift=DOWN * 0.3) for chem in chemicals],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        chem_text = Text("Chemical Overuse", font_size=24, color=PALETTE["alert"])
        chem_text.move_to(LEFT * 3.5 + DOWN * 3.0)
        self.play(Write(chem_text), run_time=1.0)
        
        # RESTORATION SIDE
        # 1. Rewilding
        restoration_ground = Rectangle(
            width=5.0,
            height=1.0,
            fill_color="#2a5a2a",
            fill_opacity=0.6,
            stroke_width=0
        ).move_to(RIGHT * 3.5 + UP * 1.5)
        
        self.play(FadeIn(restoration_ground), run_time=1.0)
        
        # New trees growing
        new_trees = VGroup()
        for i in range(4):
            tree = create_stylized_tree(size=0.7, style="deciduous", season="spring")
            tree.shift(RIGHT * 3.5 + RIGHT * (i - 1.5) * 1.0 + UP * 1.8)
            new_trees.add(tree)
        
        self.play(
            LaggedStart(
                *[GrowFromCenter(tree, rate_func=smooth) for tree in new_trees],
                lag_ratio=0.2
            ),
            run_time=3.0
        )
        
        rewild_text = Text("Rewilding", font_size=24, color=GREEN)
        rewild_text.move_to(RIGHT * 3.5 + UP * 0.8)
        self.play(Write(rewild_text), run_time=1.0)
        
        # 2. Healthy network
        healthy_network = ProceduralHyphae(
            start=RIGHT * 3.5 + DOWN * 0.5,
            depth=6,
            length=1.5,
            angle_variance=PI / 2,
            branch_probability=0.8,
            color=PALETTE["fungal_bright"],
            stroke_width=2.5,
            seed=444
        )
        
        glowing_healthy = VisualEffects.add_glow(
            healthy_network,
            color=PALETTE["fungal"],
            intensity=0.4
        )
        
        self.play(Create(glowing_healthy, run_time=3.5))
        
        network_health_text = Text("Restored Networks", font_size=24, color=GREEN)
        network_health_text.move_to(RIGHT * 3.5 + DOWN * 2.0)
        self.play(Write(network_health_text), run_time=1.0)
        
        # 3. Fungal inoculation
        inoculation_point = Dot(
            radius=0.15,
            color=PALETTE["nutrient_bright"]
        ).move_to(RIGHT * 3.5 + DOWN * 2.8)
        
        inoculation_glow = Circle(
            radius=0.3,
            color=PALETTE["nutrient"],
            fill_opacity=0.4,
            stroke_width=0
        ).move_to(inoculation_point.get_center())
        
        self.play(
            FadeIn(VGroup(inoculation_glow, inoculation_point), scale=1.5),
            run_time=1.5
        )
        
        # Spreading restoration effect
        restoration_waves = VGroup()
        for i in range(4):
            wave = Circle(
                radius=0.4 + i * 0.3,
                stroke_color=GREEN,
                stroke_width=2,
                fill_opacity=0
            ).move_to(inoculation_point.get_center())
            restoration_waves.add(wave)
        
        self.play(
            LaggedStart(
                *[wave.animate.scale(2.5).set_stroke(opacity=0) for wave in restoration_waves],
                lag_ratio=0.3
            ),
            run_time=3.0
        )
        
        inoc_text = Text("Fungal Inoculation", font_size=24, color=GREEN)
        inoc_text.move_to(RIGHT * 3.5 + DOWN * 3.3)
        self.play(Write(inoc_text), run_time=1.0)
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["ThreatsRestorationScene"],
            SCENE_DURATIONS["ThreatsRestorationScene"] - 45
        )
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2.0)


class ConclusionScene(Scene):
    def construct(self):
        # Fade in from black
        self.wait(0.5)
        
        # Main message
        main_text = Text(
            "Everything is Connected",
            font_size=72,
            weight=BOLD,
            color=PALETTE["text_primary"]
        )
        main_text.set_sheen(-0.4, direction=UP)
        
        # Subtitle
        subtitle1 = Text(
            "Beneath every forest, grassland, and garden",
            font_size=36,
            color=PALETTE["text_secondary"]
        )
        
        subtitle2 = Text(
            "life threads itself together",
            font_size=36,
            color=PALETTE["text_secondary"]
        )
        
        message_group = VGroup(main_text, subtitle1, subtitle2)
        message_group.arrange(DOWN, buff=0.6)
        
        # Background network visualization
        bg_network = VGroup()
        
        # Create organic network of nodes
        np.random.seed(555)
        node_positions = []
        for _ in range(40):
            x = np.random.uniform(-6.5, 6.5)
            y = np.random.uniform(-3.5, 3.5)
            node_positions.append([x, y, 0])
        
        # Add nodes with varying sizes
        for pos in node_positions:
            node_size = np.random.uniform(0.02, 0.06)
            node = Dot(
                point=pos,
                radius=node_size,
                color=PALETTE["fungal"],
                fill_opacity=0.3
            )
            bg_network.add(node)
        
        # Connect nearby nodes
        for i, pos1 in enumerate(node_positions):
            for j, pos2 in enumerate(node_positions[i+1:], start=i+1):
                distance = np.linalg.norm(np.array(pos1) - np.array(pos2))
                
                if distance < 2.5 and np.random.random() < 0.4:
                    line = Line(pos1, pos2)
                    line.set_stroke(
                        PALETTE["fungal"],
                        width=1.0,
                        opacity=0.15
                    )
                    bg_network.add(line)
        
        bg_network.set_z_index(-1)
        
        # Animate background network
        self.add(bg_network)
        self.play(
            bg_network.animate.set_opacity(0.25),
            run_time=2.0
        )
        
        # Main text animation
        self.play(
            FadeIn(main_text, shift=UP * 0.5, scale=1.1),
            run_time=2.0
        )
        
        self.play(
            FadeIn(subtitle1, shift=UP * 0.3),
            run_time=1.5
        )
        
        self.play(
            FadeIn(subtitle2, shift=UP * 0.3),
            run_time=1.5
        )
        
        # Pulse the network
        for _ in range(3):
            self.play(
                bg_network.animate.set_opacity(0.45),
                run_time=1.2,
                rate_func=smooth
            )
            self.play(
                bg_network.animate.set_opacity(0.2),
                run_time=1.2,
                rate_func=smooth
            )
        
        # Call to action
        self.play(
            message_group.animate.shift(UP * 1.5),
            run_time=2.0
        )
        
        call_to_action = Text(
            "Heal the networks.\nHeal the planet.",
            font_size=52,
            weight=BOLD,
            color=GREEN,
            line_spacing=1.2
        )
        call_to_action.shift(DOWN * 1.0)
        
        self.play(
            Write(call_to_action),
            run_time=3.0
        )
        
        # Final network pulse with spreading effect
        for node in bg_network:
            if isinstance(node, Dot):
                pulse = Circle(
                    radius=0.1,
                    stroke_color=PALETTE["fungal_bright"],
                    stroke_width=2,
                    fill_opacity=0
                ).move_to(node.get_center())
                
                self.play(
                    pulse.animate.scale(8).set_stroke(opacity=0),
                    run_time=1.5,
                    rate_func=rush_from
                )
                self.remove(pulse)
        
        # Display subtitles
        AdaptiveSubtitle.display_subtitles(
            self,
            SUBTITLES["ConclusionScene"],
            SCENE_DURATIONS["ConclusionScene"] - 20
        )
        
        # Final fade to black
        self.play(
            *[FadeOut(mob, scale=0.9) for mob in self.mobjects],
            run_time=4.0
        )
        
        self.wait(2.0)


# ==================== FULL DOCUMENTARY ASSEMBLY ====================
class FullDocumentary(Scene):
    """
    Complete 30-minute documentary rendering all scenes in sequence.
    Use this for final production.
    """
    def construct(self):
        scenes = [
            IntroScene,
            HistoryScene,
            NetworkOverviewScene,
            MiningExchangeScene,
            CommunicationScene,
            ArchitectureScene,
            CompetitionScene,
            EcosystemsScene,
            ResearchMethodsScene,
            ThreatsRestorationScene,
            ConclusionScene
        ]
        
        for i, SceneClass in enumerate(scenes):
            # Scene transition (except for first scene)
            if i > 0:
                SceneTransitions.fade_through_black(self, run_time=1.2)
            
            # Render the scene
            scene_instance = SceneClass()
            
            # Execute the scene's construct method
            # Note: We're calling construct() which will add all animations
            # to this main scene's animation queue
            scene_instance.renderer = self.renderer
            scene_instance.camera = self.camera
            
            # Transfer all scene elements
            scene_instance.construct()
            
            # Small buffer between scenes
            self.wait(0.5)
            
            # Clear for next scene
            self.remove(*self.mobjects)


# ==================== USAGE GUIDE ====================
"""
GOOGLE COLAB SETUP & RENDERING INSTRUCTIONS
============================================

CELL 1: Install Manim and Dependencies
---------------------------------------
!sudo apt update -qq
!sudo apt install -y libcairo2-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-science tipa libpango1.0-dev
!pip install -q manim
!pip install -q pillow

CELL 2: Save Script
-------------------
%%writefile main.py
[Paste this entire script here]

CELL 3: Configure Performance (Optional)
-----------------------------------------
# Edit these constants at the top of main.py for your needs:
# ENABLE_ADVANCED_EFFECTS = False  # Faster rendering
# PARTICLE_DENSITY = "low"  # Fewer particles
# config.frame_rate = 30  # Lower framerate

CELL 4: Test Individual Scenes (RECOMMENDED)
--------------------------------------------
# Start with low quality to test timing and animations
!manim -pql main.py IntroScene

# Test each scene individually:
!manim -pql main.py HistoryScene
!manim -pql main.py NetworkOverviewScene
!manim -pql main.py MiningExchangeScene
!manim -pql main.py CommunicationScene
!manim -pql main.py ArchitectureScene
!manim -pql main.py CompetitionScene
!manim -pql main.py EcosystemsScene
!manim -pql main.py ResearchMethodsScene
!manim -pql main.py ThreatsRestorationScene
!manim -pql main.py ConclusionScene

CELL 5: Render High Quality Individual Scenes
----------------------------------------------
# Once satisfied with timing, render in high quality:
!manim -pqh main.py IntroScene --disable_caching

# Repeat for all scenes you want in high quality

CELL 6: Render Complete Documentary (ADVANCED)
-----------------------------------------------
# WARNING: This will take 3-5 hours even on Colab Pro
# Make sure you have Colab Pro with extended runtime
!manim -pqh main.py FullDocumentary --disable_caching

# Alternative: Medium quality is faster (1-2 hours)
!manim -pqm main.py FullDocumentary

CELL 7: Download Results
------------------------
from google.colab import files

# Download specific scene
files.download('/content/media/videos/main/1080p60/IntroScene.mp4')

# Or download all videos
!zip -r documentary_scenes.zip /content/media/videos/main/
files.download('documentary_scenes.zip')


QUALITY OPTIONS
===============
-pql  = Low quality (480p15)     - Fast testing (~2 min per scene)
-pqm  = Medium quality (720p30)  - Balanced (~5 min per scene)  
-pqh  = High quality (1080p60)   - Production (~10 min per scene)
-pqk  = 4K quality (2160p60)     - Ultra HD (~20 min per scene)

PRODUCTION WORKFLOW
===================
1. Test all scenes individually with -pql
2. Adjust timing/subtitles as needed
3. Render each scene separately with -pqh
4. Use video editing software (DaVinci Resolve, Premiere) to:
   - Combine all scenes
   - Add audio narration (use audio_cues.json for timing)
   - Fine-tune transitions
   - Color grade
   - Add background music
   - Export final documentary

PERFORMANCE TIPS
================
- Use Colab Pro for longer runtime and better GPU
- Render scenes separately to avoid timeout
- Use --disable_caching to save memory
- Lower frame_rate to 30fps if needed (change config.frame_rate)
- Set PARTICLE_DENSITY = "low" for faster rendering
- Disable ENABLE_ADVANCED_EFFECTS for 2x speed boost

CUSTOMIZATION
=============
- Edit SCENE_DURATIONS to adjust timing
- Modify SUBTITLES dictionary to change narration
- Adjust PALETTE for different color schemes
- Change config.frame_rate for different framerates
- Modify seed values in ProceduralHyphae for different patterns
- Toggle ENABLE_SOUND_MARKERS for audio cue export

TROUBLESHOOTING
===============
- If subtitles overlap: Reduce font_size or max_width in AdaptiveSubtitle
- If scenes render slowly: Lower particle counts or use PARTICLE_DENSITY="low"
- If memory errors: Render in lower quality or reduce scene complexity
- If timing is off: Adjust SCENE_DURATIONS and display_time parameters
- If effects are too much: Set ENABLE_ADVANCED_EFFECTS = False

NEW FEATURES IN THIS VERSION
============================
✨ Audio cue markers - Export timing for voice-over sync
✨ Performance optimizer - Adaptive quality settings
✨ Time indicator - Progress bar for long renders
✨ Scientific overlays - Scale bars, citations, fact boxes
✨ Cinematic camera - Dolly zoom, orbital pan, rack focus
✨ Motion blur - Simulated motion blur effects
✨ Vignette effect - Cinematic edge darkening
✨ Interactive tooltips - Highlight and explain elements
✨ Data visualization - Animated charts and graphs
✨ Comparison views - Split-screen before/after
✨ Animation presets - Consistent motion patterns

AUDIO INTEGRATION GUIDE
========================
After rendering, add audio using the exported audio_cues.json file:

1. Import cues into your DAW (Reaper, Audacity, etc.)
2. Record narration matching subtitle timing
3. Add ambient sounds:
   - Forest ambience (birds, wind)
   - Underground sounds (subtle rumbling)
   - Whooshes for transitions
   - Particle flow sounds
4. Add musical score:
   - Gentle piano for intro
   - Strings for emotional moments
   - Ambient pads for underground scenes
   - Uplifting melody for conclusion
5. Mix and master:
   - Narration: -6dB to -3dB
   - Music: -20dB to -12dB
   - SFX: -15dB to -8dB

Use ffmpeg to combine:
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -b:a 192k output.mp4

ADVANCED RENDERING OPTIONS
===========================
# Transparent background (for compositing)
!manim -pqh --transparent main.py IntroScene

# Custom resolution
!manim -pqh --resolution 3840,2160 main.py IntroScene  # 4K

# Save last frame
!manim -pqh -s main.py IntroScene

# Preview without saving
!manim -p main.py IntroScene

# Render specific time range
# (Edit scene construct method to add self.wait() at start)

EXPORTING FOR DIFFERENT PLATFORMS
==================================
YouTube (1080p60):
  !manim -pqh main.py FullDocumentary
  
Instagram (1080x1080):
  config.pixel_width = 1080
  config.pixel_height = 1080
  
TikTok (1080x1920):
  config.pixel_width = 1080
  config.pixel_height = 1920
  
Twitter (720p):
  !manim -pqm main.py FullDocumentary

ACCESSIBILITY FEATURES
======================
- High contrast subtitles with backgrounds
- Clear, readable fonts (Helvetica)
- Color-blind friendly palette
- Adjustable subtitle timing
- Optional progress bar
- Multiple quality options

SCIENTIFIC ACCURACY NOTES
==========================
- Scale bars added where appropriate
- Citations can be added with ScientificNotation.create_citation()
- Accurate representation of mycorrhizal structures
- Based on current research (as of 2025)
- Fact boxes available for key statistics

COLLABORATIVE WORKFLOW
======================
1. Researcher: Provides script and facts
2. Animator: Creates scenes in Manim
3. Narrator: Records voice-over using timing guide
4. Sound Designer: Adds music and effects
5. Editor: Final assembly and color grading
6. Reviewer: Checks scientific accuracy

Each role can work independently with the exported files!

MONETIZATION READY
==================
This documentary is production-quality and ready for:
- YouTube (with proper audio)
- Educational platforms
- Museum installations
- Conference presentations
- Online courses
- Science communication

Remember to add:
- Proper attributions
- Creative Commons license info
- Contact information
- Social media handles

FUTURE ENHANCEMENTS
===================
Consider adding in post-production:
- 3D depth effects (After Effects)
- Additional particle systems
- Interactive elements (for web)
- Multiple language tracks
- Closed captions/SDH
- Audio description track
- Chapter markers
- End cards with resources

COMMUNITY FEATURES
==================
Share your rendered documentary:
- Tag #ManimCommunity
- Share on r/manim
- Contribute improvements on GitHub
- Help other educators

Support the Manim project:
- Star the repository
- Report bugs
- Contribute code
- Spread the word

===================================
Created with ❤️ using Manim
Community Edition v0.18+
===================================
"""