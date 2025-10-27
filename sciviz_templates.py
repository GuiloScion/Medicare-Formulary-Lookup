# sciviz_edu/templates/networks.py
"""
Network visualization templates for biological, neural, and social networks
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple, Optional, Callable
from dataclasses import dataclass


@dataclass
class NetworkNode:
    """Represents a node in a network"""
    id: str
    position: np.ndarray
    label: str = ""
    color: str = BLUE
    radius: float = 0.15
    properties: Dict = None
    
    def __post_init__(self):
        if self.properties is None:
            self.properties = {}


@dataclass
class NetworkEdge:
    """Represents an edge in a network"""
    source: str
    target: str
    weight: float = 1.0
    directed: bool = False
    color: str = WHITE
    properties: Dict = None
    
    def __post_init__(self):
        if self.properties is None:
            self.properties = {}


class NetworkTemplate(VGroup):
    """Base template for network visualizations"""
    
    def __init__(
        self,
        nodes: List[NetworkNode],
        edges: List[NetworkEdge],
        show_labels: bool = True,
        animate_creation: bool = True,
        layout: str = "spring",
        **kwargs
    ):
        super().__init__(**kwargs)
        
        self.node_data = {n.id: n for n in nodes}
        self.edge_data = edges
        self.show_labels = show_labels
        self.layout_type = layout
        
        # Create visual elements
        self.node_mobjects: Dict[str, Dot] = {}
        self.edge_mobjects: List[Line] = []
        self.label_mobjects: Dict[str, Text] = {}
        
        self._build_network()
    
    def _build_network(self):
        """Construct network visualization"""
        # Create nodes
        for node_id, node in self.node_data.items():
            dot = Dot(
                point=node.position,
                radius=node.radius,
                color=node.color
            )
            dot.set_fill(node.color, opacity=0.9)
            self.node_mobjects[node_id] = dot
            self.add(dot)
            
            if self.show_labels and node.label:
                label = Text(node.label, font_size=20)
                label.next_to(dot, UP, buff=0.1)
                self.label_mobjects[node_id] = label
                self.add(label)
        
        # Create edges
        for edge in self.edge_data:
            source_pos = self.node_mobjects[edge.source].get_center()
            target_pos = self.node_mobjects[edge.target].get_center()
            
            if edge.directed:
                line = Arrow(
                    source_pos,
                    target_pos,
                    buff=self.node_data[edge.source].radius,
                    stroke_width=2 * edge.weight,
                    color=edge.color
                )
            else:
                line = Line(
                    source_pos,
                    target_pos,
                    stroke_width=2 * edge.weight,
                    color=edge.color
                )
            
            self.edge_mobjects.append(line)
            self.add(line)
        
        # Move edges to back
        for edge in self.edge_mobjects:
            edge.set_z_index(-1)
    
    def highlight_node(self, node_id: str, color: str = YELLOW) -> Animation:
        """Highlight a specific node"""
        node = self.node_mobjects[node_id]
        return Indicate(node, color=color, scale_factor=1.3)
    
    def highlight_path(self, path: List[str], color: str = YELLOW) -> List[Animation]:
        """Highlight a path through the network"""
        anims = []
        for i in range(len(path) - 1):
            source, target = path[i], path[i + 1]
            # Find edge
            for edge_mob, edge_data in zip(self.edge_mobjects, self.edge_data):
                if edge_data.source == source and edge_data.target == target:
                    anims.append(edge_mob.animate.set_color(color).set_stroke(width=4))
                    break
        return anims
    
    def animate_flow(
        self,
        source: str,
        target: str,
        particle_color: str = YELLOW,
        particle_count: int = 5
    ) -> List[Animation]:
        """Animate particles flowing along an edge"""
        source_pos = self.node_mobjects[source].get_center()
        target_pos = self.node_mobjects[target].get_center()
        
        path = Line(source_pos, target_pos)
        particles = VGroup(*[
            Dot(radius=0.05, color=particle_color).move_to(source_pos)
            for _ in range(particle_count)
        ])
        
        return [
            MoveAlongPath(p, path, run_time=2.0, rate_func=linear)
            for p in particles
        ]


class BiologicalNetwork(NetworkTemplate):
    """Template for biological networks (mycorrhizal, food webs, etc.)"""
    
    def __init__(
        self,
        num_plants: int = 5,
        num_fungi: int = 3,
        connectivity: float = 0.6,
        show_nutrient_flow: bool = True,
        **kwargs
    ):
        # Generate biological network structure
        nodes, edges = self._generate_biological_network(
            num_plants, num_fungi, connectivity
        )
        
        super().__init__(nodes, edges, **kwargs)
        self.show_nutrient_flow = show_nutrient_flow
    
    def _generate_biological_network(
        self,
        num_plants: int,
        num_fungi: int,
        connectivity: float
    ) -> Tuple[List[NetworkNode], List[NetworkEdge]]:
        """Generate a biological network structure"""
        nodes = []
        edges = []
        
        # Create plant nodes (above ground)
        for i in range(num_plants):
            x = (i - num_plants / 2) * 2
            y = 2.0 + random.uniform(-0.3, 0.3)
            nodes.append(NetworkNode(
                id=f"plant_{i}",
                position=np.array([x, y, 0]),
                label=f"P{i+1}",
                color="#2d7f3e",
                radius=0.2
            ))
        
        # Create fungal nodes (below ground)
        for i in range(num_fungi):
            x = (i - num_fungi / 2) * 2.5
            y = -1.5 + random.uniform(-0.3, 0.3)
            nodes.append(NetworkNode(
                id=f"fungus_{i}",
                position=np.array([x, y, 0]),
                label=f"F{i+1}",
                color="#19a7a4",
                radius=0.15
            ))
        
        # Create connections
        for plant_idx in range(num_plants):
            for fungus_idx in range(num_fungi):
                if random.random() < connectivity:
                    edges.append(NetworkEdge(
                        source=f"plant_{plant_idx}",
                        target=f"fungus_{fungus_idx}",
                        weight=random.uniform(0.5, 1.5),
                        color="#7fb05d"
                    ))
        
        return nodes, edges
    
    def animate_nutrient_exchange(self, run_time: float = 4.0) -> List[Animation]:
        """Animate bidirectional nutrient flow"""
        anims = []
        
        # Carbon flow (plants to fungi)
        for edge in self.edge_data[:min(3, len(self.edge_data))]:
            source_pos = self.node_mobjects[edge.source].get_center()
            target_pos = self.node_mobjects[edge.target].get_center()
            
            path = Line(source_pos, target_pos)
            particle = Dot(radius=0.06, color="#ffd166")
            particle.move_to(source_pos)
            
            anims.append(MoveAlongPath(particle, path, run_time=run_time))
        
        return anims


class NeuralNetwork(NetworkTemplate):
    """Template for neural network visualizations"""
    
    def __init__(
        self,
        layer_sizes: List[int] = [3, 4, 2],
        activation_function: str = "relu",
        show_weights: bool = False,
        **kwargs
    ):
        nodes, edges = self._generate_neural_network(layer_sizes, show_weights)
        super().__init__(nodes, edges, show_labels=False, **kwargs)
        
        self.layer_sizes = layer_sizes
        self.activation_function = activation_function
    
    def _generate_neural_network(
        self,
        layer_sizes: List[int],
        show_weights: bool
    ) -> Tuple[List[NetworkNode], List[NetworkEdge]]:
        """Generate neural network structure"""
        nodes = []
        edges = []
        
        layer_spacing = 3.0
        node_spacing = 0.8
        
        # Create nodes for each layer
        node_counter = 0
        for layer_idx, size in enumerate(layer_sizes):
            x = (layer_idx - len(layer_sizes) / 2) * layer_spacing
            
            for neuron_idx in range(size):
                y = (neuron_idx - size / 2) * node_spacing
                
                # Color based on layer
                if layer_idx == 0:
                    color = "#3d5a80"  # Input layer
                elif layer_idx == len(layer_sizes) - 1:
                    color = "#ee6c4d"  # Output layer
                else:
                    color = "#98c1d9"  # Hidden layers
                
                nodes.append(NetworkNode(
                    id=f"neuron_{node_counter}",
                    position=np.array([x, y, 0]),
                    color=color,
                    radius=0.15,
                    properties={"layer": layer_idx, "index": neuron_idx}
                ))
                node_counter += 1
        
        # Create connections (fully connected between adjacent layers)
        node_idx = 0
        for layer_idx in range(len(layer_sizes) - 1):
            layer_size = layer_sizes[layer_idx]
            next_layer_size = layer_sizes[layer_idx + 1]
            
            for i in range(layer_size):
                for j in range(next_layer_size):
                    source_id = f"neuron_{node_idx + i}"
                    target_id = f"neuron_{node_idx + layer_size + j}"
                    
                    weight = random.uniform(0.3, 1.0) if show_weights else 1.0
                    
                    edges.append(NetworkEdge(
                        source=source_id,
                        target=target_id,
                        weight=weight,
                        color=WHITE,
                        directed=True
                    ))
            
            node_idx += layer_size
        
        return nodes, edges
    
    def animate_forward_pass(
        self,
        input_values: List[float],
        run_time: float = 3.0
    ) -> List[Animation]:
        """Animate a forward pass through the network"""
        anims = []
        
        # Activate input layer
        for i, val in enumerate(input_values):
            node_id = f"neuron_{i}"
            intensity = abs(val)
            anims.append(
                self.node_mobjects[node_id].animate.set_fill(
                    YELLOW, opacity=intensity
                )
            )
        
        return anims


class SocialNetwork(NetworkTemplate):
    """Template for social network visualizations"""
    
    def __init__(
        self,
        num_nodes: int = 20,
        clustering: float = 0.3,
        show_communities: bool = True,
        **kwargs
    ):
        nodes, edges = self._generate_social_network(num_nodes, clustering)
        super().__init__(nodes, edges, **kwargs)
        
        self.show_communities = show_communities
    
    def _generate_social_network(
        self,
        num_nodes: int,
        clustering: float
    ) -> Tuple[List[NetworkNode], List[NetworkEdge]]:
        """Generate a social network with community structure"""
        nodes = []
        edges = []
        
        # Use spring layout
        angles = np.linspace(0, 2 * np.pi, num_nodes, endpoint=False)
        radius = 3.0
        
        # Create communities
        num_communities = 3
        community_colors = ["#e76f51", "#2a9d8f", "#e9c46a"]
        
        for i in range(num_nodes):
            community = i % num_communities
            angle = angles[i] + random.uniform(-0.1, 0.1)
            r = radius + random.uniform(-0.5, 0.5)
            
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            
            nodes.append(NetworkNode(
                id=f"person_{i}",
                position=np.array([x, y, 0]),
                color=community_colors[community],
                radius=0.12,
                properties={"community": community}
            ))
        
        # Create edges (higher probability within communities)
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                same_community = (i % num_communities) == (j % num_communities)
                prob = clustering if same_community else clustering * 0.2
                
                if random.random() < prob:
                    edges.append(NetworkEdge(
                        source=f"person_{i}",
                        target=f"person_{j}",
                        color=GRAY,
                        weight=0.5
                    ))
        
        return nodes, edges


# ============================================
# Factory Functions
# ============================================

def create_biological_network(
    num_plants: int = 5,
    num_fungi: int = 3,
    connectivity: float = 0.6,
    **kwargs
) -> BiologicalNetwork:
    """Create a biological network template"""
    return BiologicalNetwork(
        num_plants=num_plants,
        num_fungi=num_fungi,
        connectivity=connectivity,
        **kwargs
    )


def create_neural_network(
    layer_sizes: List[int] = [3, 4, 2],
    **kwargs
) -> NeuralNetwork:
    """Create a neural network template"""
    return NeuralNetwork(layer_sizes=layer_sizes, **kwargs)


def create_social_network(
    num_nodes: int = 20,
    clustering: float = 0.3,
    **kwargs
) -> SocialNetwork:
    """Create a social network template"""
    return SocialNetwork(
        num_nodes=num_nodes,
        clustering=clustering,
        **kwargs
    )


# ============================================
# Example Usage
# ============================================

if __name__ == "__main__":
    from sciviz_edu.core.scene import EducationalScene, LearningObjective, BloomLevel
    
    class NetworkComparisonScene(EducationalScene):
        def construct(self):
            self.setup_metadata(
                title="Network Types Comparison",
                description="Compare different types of networks"
            )
            
            self.add_objective(
                LearningObjective(
                    id="obj_1",
                    description="Identify structural differences between network types",
                    bloom_level=BloomLevel.ANALYZE,
                    assessment_method="visual_comparison"
                )
            )
            
            # Create three networks side by side
            bio_net = create_biological_network(num_plants=3, num_fungi=2)
            bio_net.scale(0.6).shift(LEFT * 4)
            
            neural_net = create_neural_network(layer_sizes=[2, 3, 2])
            neural_net.scale(0.6)
            
            social_net = create_social_network(num_nodes=12, clustering=0.4)
            social_net.scale(0.6).shift(RIGHT * 4)
            
            # Labels
            bio_label = Text("Biological", font_size=24).next_to(bio_net, UP)
            neural_label = Text("Neural", font_size=24).next_to(neural_net, UP)
            social_label = Text("Social", font_size=24).next_to(social_net, UP)
            
            # Animate
            self.play(
                LaggedStart(
                    AnimationGroup(Create(bio_net), Write(bio_label)),
                    AnimationGroup(Create(neural_net), Write(neural_label)),
                    AnimationGroup(Create(social_net), Write(social_label)),
                    lag_ratio=0.3
                ),
                run_time=4
            )
            
            self.wait(2)