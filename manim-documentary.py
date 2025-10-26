"""
Mycorrhizal Documentary - Manim Animation
A 10-minute scientific documentary with animations

Installation:
pip install manim
pip install gtts

Usage:
manim -pql mycorrhizal_documentary.py MycorrhizalDocumentary

For high quality:
manim -pqh mycorrhizal_documentary.py MycorrhizalDocumentary

For 4K:
manim -pqk mycorrhizal_documentary.py MycorrhizalDocumentary
"""

from manim import *
from gtts import gTTS
import os

class MycorrhizalDocumentary(Scene):
    def construct(self):
        # Generate all audio files first
        self.generate_all_audio()
        
        # Run all segments
        self.segment_01_opening()
        self.segment_02_introduction()
        self.segment_03_colonization()
        self.segment_04_carbon_flow()
        self.segment_05_nutrient_exchange()
        self.segment_06_network()
        self.segment_07_transfer()
        self.segment_08_defense()
        self.segment_09_complexity()
        self.segment_10_conclusion()
        self.segment_11_closing()
    
    def generate_all_audio(self):
        """Generate all TTS audio files"""
        segments = [
            ("In the cathedral silence of an old-growth forest, a secret conversation unfolds. Not in the rustling canopy above, but in the darkness beneath our feet. Here, in the soil, an ancient partnership sustains the very lungs of our planet.", "01_opening"),
            ("These are mycorrhizal fungi—from the Greek 'mykes' meaning fungus, and 'rhiza' meaning root. For over four hundred million years, since plants first colonized land, this alliance has shaped terrestrial ecosystems. Today, ninety percent of all land plants depend upon it.", "02_intro"),
            ("The fungal partner extends thread-like hyphae—structures so fine that a single gram of forest soil may contain several kilometers of them. These hyphae colonize plant roots, but they don't simply attach. They integrate. In ectomycorrhizae, they form a sheath around root tips and penetrate between cortical cells. In endomycorrhizae, they actually breach the cell wall, though never the cell membrane itself.", "03_colonization"),
            ("What drives this intimacy? Economics. The tree, through photosynthesis, is a factory of carbohydrates. Sugars flow from leaves to roots, and from roots to fungi—up to thirty percent of all photosynthate produced by the tree. This is not charity. This is commerce.", "04_carbon"),
            ("In exchange, the fungus offers what the tree cannot easily obtain: reach. While root hairs might extend mere millimeters into soil, fungal hyphae venture centimeters, even meters beyond. Their surface area for absorption exceeds that of roots by a factor of one hundred or more. They mine the soil for phosphorus—often locked in insoluble compounds—and nitrogen, and deliver water during drought.", "05_nutrients"),
            ("But the network doesn't stop at a single tree. Mycorrhizal fungi are rarely monogamous. A single fungal individual may connect to multiple trees, even different species. And a single tree may host dozens of fungal partners. What emerges is a common mycorrhizal network—what some researchers have termed the 'wood wide web.'", "06_network"),
            ("Through these networks, resources move between trees. Older 'mother trees,' with deeper roots and established fungal partnerships, have been shown to transfer carbon to younger seedlings in their shadow—seedlings that cannot yet photosynthesize enough to survive alone. It's not altruism in the human sense, but it functions as such.", "07_transfer"),
            ("The network carries more than nutrients. When a tree is attacked by insects, it produces defense chemicals. But it also sends signals through the mycorrhizal network—chemical warnings that prompt neighboring trees to elevate their own defenses before they're touched. The forest, it seems, has an immune system.", "08_defense"),
            ("Yet this partnership is not without its darker aspects. Some plants have lost their chlorophyll entirely, becoming mycoheterotrophs—parasites on the network, taking carbon without contributing. And certain fungi, in times of scarcity, may extract more from their hosts than they provide. Symbiosis exists on a continuum between mutualism and exploitation.", "09_complexity"),
            ("As we stand in the forest, it's worth remembering: we're not looking at individuals. We're looking at a superorganism—a distributed intelligence where tree and fungus are as interconnected as neurons in a brain. Every footstep falls upon billions of transactions, an economy far older than our own, operating on principles we're only beginning to decode.", "10_conclusion"),
            ("The forests we see are merely the fruiting bodies of a deeper collaboration. And in protecting them, we protect not trees alone, but the ancient covenant that made the green world possible.", "11_closing")
        ]
        
        os.makedirs("audio", exist_ok=True)
        for text, filename in segments:
            audio_path = f"audio/segment_{filename}.mp3"
            if not os.path.exists(audio_path):
                print(f"Generating audio: {filename}")
                tts = gTTS(text=text, lang='en', tld='co.uk', slow=False)
                tts.save(audio_path)
    
    def add_voiceover(self, filename):
        """Add voiceover audio to scene"""
        audio_path = f"audio/segment_{filename}.mp3"
        if os.path.exists(audio_path):
            self.add_sound(audio_path)
    
    def segment_01_opening(self):
        """Opening sequence - 45 seconds"""
        # Dark forest atmosphere
        self.camera.background_color = "#0a1810"
        
        # Title sequence
        title = Text("THE HIDDEN NETWORK", font_size=72, weight=BOLD)
        title.set_color_by_gradient(GREEN, YELLOW)
        
        subtitle = Text("Mycorrhizal Fungi & Trees", font_size=36)
        subtitle.set_color(GREEN_C)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        tagline = Text("A Symbiotic Documentary", font_size=24, slant=ITALIC)
        tagline.set_color(GREY_A)
        tagline.next_to(subtitle, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle, tagline)
        
        self.add_voiceover("01_opening")
        
        # Fade in title
        self.play(FadeIn(title_group), run_time=3)
        self.wait(2)
        
        # Zoom down to soil level
        soil_line = Line(LEFT * 7, RIGHT * 7, color=ORANGE).shift(DOWN * 2)
        soil_rect = Rectangle(width=14, height=4, fill_opacity=0.3, color=YELLOW_E)
        soil_rect.next_to(soil_line, DOWN, buff=0)
        
        self.play(
            title_group.animate.shift(UP * 4).scale(0.5),
            Create(soil_line),
            FadeIn(soil_rect),
            run_time=2
        )
        
        # Create underground network visualization
        network_dots = VGroup(*[
            Dot(point=[np.random.uniform(-6, 6), np.random.uniform(-3.5, -2.5), 0], 
                radius=0.05, color=ORANGE)
            for _ in range(50)
        ])
        
        self.play(LaggedStart(*[FadeIn(dot) for dot in network_dots], lag_ratio=0.02))
        self.wait(3)
        
        self.play(FadeOut(title_group), FadeOut(soil_line), FadeOut(soil_rect), FadeOut(network_dots))
    
    def segment_02_introduction(self):
        """Introduction to mycorrhizae - 55 seconds"""
        self.camera.background_color = "#2a1a0a"
        
        self.add_voiceover("02_intro")
        
        # Title
        title = Text("The Ancient Alliance", font_size=48, weight=BOLD, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Draw root system
        root = VGroup()
        root_trunk = Line(ORIGIN, DOWN * 2, color=YELLOW_E, stroke_width=8)
        root.add(root_trunk)
        
        # Branch roots
        for i in range(6):
            angle = -60 + i * 24
            length = 1.5 + np.random.random() * 0.5
            branch = Line(
                DOWN * 2, 
                DOWN * 2 + np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle)), 0]) * length,
                color=YELLOW_E,
                stroke_width=4
            )
            root.add(branch)
        
        root.shift(UP * 0.5)
        self.play(Create(root), run_time=2)
        
        # Add fungal hyphae
        hyphae = VGroup()
        for i in range(12):
            start = root[1 + i % 6].get_end()
            angle = np.random.uniform(-90, 90)
            length = np.random.uniform(1, 2)
            end = start + np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle)), 0]) * length
            
            hypha = Line(start, end, color=ORANGE, stroke_width=2)
            hyphae.add(hypha)
        
        self.play(LaggedStart(*[Create(h) for h in hyphae], lag_ratio=0.1), run_time=3)
        
        # Timeline
        timeline = Text("~407 Million Years Ago", font_size=32, color=GREY_A)
        timeline.to_edge(DOWN)
        self.play(FadeIn(timeline))
        self.wait(2)
        
        # Statistics
        stat = Text("90% of land plants\ndepend on mycorrhizae", font_size=28, color=GREEN)
        stat.next_to(timeline, UP, buff=0.5)
        self.play(FadeIn(stat))
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, root, hyphae, timeline, stat)))
    
    def segment_03_colonization(self):
        """Colonization process - 60 seconds"""
        self.camera.background_color = "#1a1410"
        
        self.add_voiceover("03_colonization")
        
        title = Text("Colonization", font_size=48, weight=BOLD, color=ORANGE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Draw root cell
        cell = Rectangle(width=4, height=3, color=YELLOW_E, stroke_width=3)
        cell_label = Text("Root Cortical Cell", font_size=24, color=GREY_A)
        cell_label.next_to(cell, UP)
        
        self.play(Create(cell), Write(cell_label))
        
        # Show hyphae penetrating
        penetration_points = [
            cell.get_left() + RIGHT * 0.3,
            cell.get_bottom() + UP * 0.3,
            cell.get_right() + LEFT * 0.3
        ]
        
        hyphae_entering = VGroup()
        for point in penetration_points:
            external = Line(point + LEFT * 2, point, color=ORANGE, stroke_width=3)
            internal = Line(point, point + (cell.get_center() - point) * 0.6, color=ORANGE, stroke_width=2)
            hyphae_entering.add(external, internal)
        
        self.play(LaggedStart(*[Create(h) for h in hyphae_entering], lag_ratio=0.3), run_time=3)
        
        # Arbuscule formation (tree-like structure inside)
        arbuscule = VGroup()
        center = cell.get_center()
        
        def create_branch(start, angle, depth, max_depth=3):
            if depth > max_depth:
                return VGroup()
            
            length = 0.4 / (depth + 1)
            end = start + np.array([np.cos(angle), np.sin(angle), 0]) * length
            line = Line(start, end, color=ORANGE, stroke_width=6 - depth)
            
            branches = VGroup(line)
            if depth < max_depth:
                branches.add(create_branch(end, angle - 0.5, depth + 1, max_depth))
                branches.add(create_branch(end, angle + 0.5, depth + 1, max_depth))
            
            return branches
        
        arbuscule = create_branch(center, -PI/2, 0, 3)
        
        caption = Text("Arbuscular Mycorrhizae", font_size=24, color=ORANGE, slant=ITALIC)
        caption.to_edge(DOWN)
        
        self.play(Create(arbuscule), run_time=3)
        self.play(Write(caption))
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, cell, cell_label, hyphae_entering, arbuscule, caption)))
    
    def segment_04_carbon_flow(self):
        """Carbon flow from tree to fungus - 55 seconds"""
        self.camera.background_color = "#0a1a2a"
        
        self.add_voiceover("04_carbon")
        
        title = Text("Carbon Flow", font_size=48, weight=BOLD, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Draw simple tree
        tree_trunk = Rectangle(width=0.5, height=2, fill_opacity=0.8, color=YELLOW_E)
        tree_trunk.shift(UP * 1.5)
        
        tree_canopy = Circle(radius=1.5, fill_opacity=0.6, color=GREEN)
        tree_canopy.next_to(tree_trunk, UP, buff=0)
        
        # Sun
        sun = Circle(radius=0.4, fill_opacity=0.8, color=YELLOW).shift(UP * 3 + LEFT * 4)
        rays = VGroup(*[
            Line(sun.get_center(), sun.get_center() + np.array([np.cos(a), np.sin(a), 0]) * 0.7, color=YELLOW)
            for a in np.linspace(0, TAU, 12, endpoint=False)
        ])
        
        self.play(FadeIn(tree_trunk), FadeIn(tree_canopy), FadeIn(sun), Create(rays))
        
        # Photosynthesis annotation
        photo_eq = MathTex(r"6CO_2 + 6H_2O \rightarrow C_6H_{12}O_6", font_size=32, color=GREEN)
        photo_eq.next_to(tree_canopy, RIGHT, buff=1)
        self.play(Write(photo_eq))
        self.wait(2)
        
        # Sugar molecules flowing down
        sugars = VGroup(*[
            Circle(radius=0.1, fill_opacity=0.8, color=YELLOW).move_to(tree_canopy.get_bottom())
            for _ in range(8)
        ])
        
        # Animate sugar flow
        for i, sugar in enumerate(sugars):
            self.play(
                sugar.animate.shift(DOWN * 3.5),
                run_time=1,
                rate_func=linear
            )
            if i < len(sugars) - 1:
                self.wait(0.2)
        
        # Percentage annotation
        percentage = Text("10-30% of\nphotosynthate", font_size=28, color=YELLOW)
        percentage.shift(DOWN * 2.5)
        self.play(FadeIn(percentage))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, tree_trunk, tree_canopy, sun, rays, photo_eq, sugars, percentage)))
    
    def segment_05_nutrient_exchange(self):
        """Nutrient exchange - 60 seconds"""
        self.camera.background_color = "#1a1510"
        
        self.add_voiceover("05_nutrients")
        
        title = Text("Nutrient Exchange", font_size=48, weight=BOLD, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Root vs Hyphae reach comparison
        root_line = Line(ORIGIN, RIGHT * 2, color=YELLOW_E, stroke_width=6)
        root_line.shift(LEFT * 1 + UP * 1)
        root_label = Text("Root reach: mm", font_size=24, color=GREY_A)
        root_label.next_to(root_line, LEFT)
        
        hyphae_line = Line(ORIGIN, RIGHT * 6, color=ORANGE, stroke_width=3)
        hyphae_line.shift(LEFT * 1 + DOWN * 1)
        hyphae_label = Text("Hyphae reach: cm-m", font_size=24, color=GREY_A)
        hyphae_label.next_to(hyphae_line, LEFT)
        
        self.play(
            Create(root_line), Write(root_label),
            Create(hyphae_line), Write(hyphae_label),
            run_time=2
        )
        self.wait(2)
        
        # Show nutrients being absorbed
        nutrients = VGroup()
        nutrient_types = [
            (BLUE, r"H_2O", "Water"),
            (PURPLE, r"PO_4^{3-}", "Phosphorus"),
            (GREEN, r"NH_4^+", "Nitrogen")
        ]
        
        for i, (color, formula, name) in enumerate(nutrient_types):
            y_pos = -2 + i * 0.8
            molecule = MathTex(formula, font_size=36, color=color)
            molecule.shift(RIGHT * 4 + UP * y_pos)
            label = Text(name, font_size=20, color=GREY_A)
            label.next_to(molecule, RIGHT)
            nutrients.add(VGroup(molecule, label))
        
        # Animate nutrients moving toward root
        for nutrient_group in nutrients:
            self.play(nutrient_group.animate.shift(LEFT * 7), run_time=1.5)
        
        # Surface area stat
        stat = Text("100x surface area increase", font_size=32, color=BLUE, weight=BOLD)
        stat.to_edge(DOWN)
        self.play(FadeIn(stat))
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, root_line, root_label, hyphae_line, hyphae_label, nutrients, stat)))
    
    def segment_06_network(self):
        """Wood Wide Web network - 50 seconds"""
        self.camera.background_color = "#0a0a1a"
        
        self.add_voiceover("06_network")
        
        title = Text("The Wood Wide Web", font_size=48, weight=BOLD, color=ORANGE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create multiple trees
        trees = VGroup()
        tree_positions = [LEFT * 4, LEFT * 1.5, RIGHT * 1.5, RIGHT * 4, UP * 2]
        
        for pos in tree_positions:
            trunk = Rectangle(width=0.3, height=1, fill_opacity=0.8, color=YELLOW_E)
            canopy = Circle(radius=0.7, fill_opacity=0.6, color=GREEN)
            canopy.next_to(trunk, UP, buff=0)
            tree = VGroup(trunk, canopy).move_to(pos)
            trees.add(tree)
        
        self.play(LaggedStart(*[FadeIn(tree) for tree in trees], lag_ratio=0.2))
        
        # Create network connections
        connections = VGroup()
        for i in range(len(trees)):
            for j in range(i + 1, len(trees)):
                if np.random.random() > 0.3:  # 70% connection probability
                    line = Line(
                        trees[i].get_bottom(),
                        trees[j].get_bottom(),
                        color=ORANGE,
                        stroke_width=2
                    )
                    connections.add(line)
        
        self.play(LaggedStart(*[Create(conn) for conn in connections], lag_ratio=0.1), run_time=3)
        
        # Pulse effect on connections
        self.play(
            *[conn.animate.set_stroke(width=4, opacity=0.8) for conn in connections],
            run_time=0.5
        )
        self.play(
            *[conn.animate.set_stroke(width=2, opacity=0.5) for conn in connections],
            run_time=0.5
        )
        
        # Caption
        caption = Text("Common Mycorrhizal Networks (CMNs)", font_size=28, color=ORANGE)
        caption.to_edge(DOWN)
        self.play(FadeIn(caption))
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, trees, connections, caption)))
    
    def segment_07_transfer(self):
        """Mother tree transfer - 55 seconds"""
        self.camera.background_color = "#1a2015"
        
        self.add_voiceover("07_transfer")
        
        title = Text("Mother Trees", font_size=48, weight=BOLD, color=GREEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Large mother tree
        mother_trunk = Rectangle(width=0.8, height=2.5, fill_opacity=0.8, color=YELLOW_E)
        mother_trunk.shift(LEFT * 3)
        mother_canopy = Circle(radius=1.5, fill_opacity=0.7, color=GREEN)
        mother_canopy.next_to(mother_trunk, UP, buff=0)
        mother_label = Text("Mother Tree", font_size=20, color=GREEN, weight=BOLD)
        mother_label.next_to(mother_canopy, UP)
        
        # Small seedling
        seedling_trunk = Rectangle(width=0.2, height=0.6, fill_opacity=0.8, color=YELLOW_E)
        seedling_trunk.shift(RIGHT * 3)
        seedling_canopy = Circle(radius=0.4, fill_opacity=0.5, color=GREEN)
        seedling_canopy.next_to(seedling_trunk, UP, buff=0)
        seedling_label = Text("Seedling", font_size=20, color=GREEN)
        seedling_label.next_to(seedling_canopy, UP)
        
        self.play(
            FadeIn(VGroup(mother_trunk, mother_canopy, mother_label)),
            FadeIn(VGroup(seedling_trunk, seedling_canopy, seedling_label)),
            run_time=2
        )
        
        # Network connection
        connection = Line(
            mother_trunk.get_bottom() + DOWN * 0.5,
            seedling_trunk.get_bottom() + DOWN * 0.5,
            color=ORANGE,
            stroke_width=4
        )
        self.play(Create(connection))
        
        # Transfer particles
        particles = VGroup(*[
            Circle(radius=0.08, fill_opacity=0.9, color=YELLOW)
            for _ in range(10)
        ])
        
        for particle in particles:
            particle.move_to(mother_trunk.get_bottom() + DOWN * 0.5)
            self.play(
                particle.animate.move_to(seedling_trunk.get_bottom() + DOWN * 0.5),
                run_time=1,
                rate_func=smooth
            )
            self.remove(particle)
        
        # Research citation
        citation = Text("Simard et al. (1997)", font_size=24, color=GREY_A, slant=ITALIC)
        citation.to_edge(DOWN)
        self.play(FadeIn(citation))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, mother_trunk, mother_canopy, mother_label, 
                                  seedling_trunk, seedling_canopy, seedling_label, 
                                  connection, citation)))
    
    def segment_08_defense(self):
        """Forest defense system - 50 seconds"""
        self.camera.background_color = "#2a0a0a"
        
        self.add_voiceover("08_defense")
        
        title = Text("Forest Defense System", font_size=48, weight=BOLD, color=RED)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Tree under attack
        attacked_tree = VGroup(
            Rectangle(width=0.5, height=1.5, fill_opacity=0.8, color=YELLOW_E),
            Circle(radius=1, fill_opacity=0.6, color=GREEN)
        )
        attacked_tree[1].next_to(attacked_tree[0], UP, buff=0)
        attacked_tree.shift(LEFT * 3)
        
        # Neighboring trees
        neighbor1 = VGroup(
            Rectangle(width=0.4, height=1.2, fill_opacity=0.8, color=YELLOW_E),
            Circle(radius=0.8, fill_opacity=0.6, color=GREEN)
        )
        neighbor1[1].next_to(neighbor1[0], UP, buff=0)
        neighbor1.shift(RIGHT * 1)
        
        neighbor2 = VGroup(
            Rectangle(width=0.4, height=1.2, fill_opacity=0.8, color=YELLOW_E),
            Circle(radius=0.8, fill_opacity=0.6, color=GREEN)
        )
        neighbor2[1].next_to(neighbor2[0], UP, buff=0)
        neighbor2.shift(RIGHT * 4)
        
        trees = VGroup(attacked_tree, neighbor1, neighbor2)
        self.play(FadeIn(trees))
        
        # Show attack (insects)
        insects = VGroup(*[
            Dot(color=RED, radius=0.1).move_to(attacked_tree[1].get_center() + 
                np.array([np.random.uniform(-0.8, 0.8), np.random.uniform(-0.8, 0.8), 0]))
            for _ in range(8)
        ])
        self.play(FadeIn(insects))
        
        # Alert effect on attacked tree
        alert_circle = Circle(radius=1.3, color=RED, stroke_width=3)
        alert_circle.move_to(attacked_tree.get_center())
        self.play(Create(alert_circle), run_time=0.5)
        self.play(FadeOut(alert_circle), run_time=0.5)
        
        # Network connections
        connections = VGroup(
            Line(attacked_tree[0].get_bottom() + DOWN * 0.3, 
                 neighbor1[0].get_bottom() + DOWN * 0.3, 
                 color=ORANGE, stroke_width=3),
            Line(neighbor1[0].get_bottom() + DOWN * 0.3, 
                 neighbor2[0].get_bottom() + DOWN * 0.3, 
                 color=ORANGE, stroke_width=3)
        )
        self.play(Create(connections))
        
        # Signal propagation
        signal1 = Dot(color=YELLOW, radius=0.15)
        signal1.move_to(attacked_tree[0].get_bottom() + DOWN * 0.3)
        
        self.play(signal1.animate.move_to(neighbor1[0].get_bottom() + DOWN * 0.3), run_time=1.5)
        
        # Neighbor 1 activates defense
        defense1 = Circle(radius=1, color=GREEN, stroke_width=3)
        defense1.move_to(neighbor1.get_center())
        self.play(Create(defense1), run_time=0.5)
        
        # Signal continues
        signal2 = Dot(color=YELLOW, radius=0.15)
        signal2.move_to(neighbor1[0].get_bottom() + DOWN * 0.3)
        self.play(signal2.animate.move_to(neighbor2[0].get_bottom() + DOWN * 0.3), run_time=1.5)
        
        # Neighbor 2 activates defense
        defense2 = Circle(radius=1, color=GREEN, stroke_width=3)
        defense2.move_to(neighbor2.get_center())
        self.play(Create(defense2), run_time=0.5)
        
        # Caption
        caption = Text("Chemical warning signals via CMN", font_size=28, color=YELLOW)
        caption.to_edge(DOWN)
        self.play(FadeIn(caption))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, trees, insects, connections, defense1, defense2, caption)))
    
    def segment_09_complexity(self):
        """Parasitism and complexity - 55 seconds"""
        self.camera.background_color = "#1a0a1a"
        
        self.add_voiceover("09_complexity")
        
        title = Text("The Complexity", font_size=48, weight=BOLD, color=PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create spectrum
        spectrum_line = Line(LEFT * 5, RIGHT * 5, stroke_width=3)
        spectrum_line.set_color_by_gradient(GREEN, PURPLE, RED)
        spectrum_line.shift(UP * 1)
        
        mutualism_label = Text("Mutualism", font_size=28, color=GREEN)
        mutualism_label.next_to(spectrum_line.get_left(), DOWN)
        
        parasitism_label = Text("Parasitism", font_size=28, color=RED)
        parasitism_label.next_to(spectrum_line.get_right(), DOWN)
        
        self.play(
            Create(spectrum_line),
            Write(mutualism_label),
            Write(parasitism_label)
        )
        
        # Normal plant with chlorophyll
        normal_plant = VGroup(
            Rectangle(width=0.3, height=1, fill_opacity=0.8, color=YELLOW_E),
            Circle(radius=0.6, fill_opacity=0.7, color=GREEN)
        )
        normal_plant[1].next_to(normal_plant[0], UP, buff=0)
        normal_plant.shift(LEFT * 3 + DOWN * 2)
        normal_label = Text("Photosynthetic", font_size=20, color=GREEN)
        normal_label.next_to(normal_plant, DOWN)
        
        # Mycoheterotroph (ghost plant - no chlorophyll)
        ghost_plant = VGroup(
            Rectangle(width=0.3, height=1, fill_opacity=0.8, color=GREY),
            Circle(radius=0.6, fill_opacity=0.4, color=WHITE)
        )
        ghost_plant[1].next_to(ghost_plant[0], UP, buff=0)
        ghost_plant.shift(RIGHT * 3 + DOWN * 2)
        ghost_label = Text("Mycoheterotroph", font_size=20, color=PURPLE)
        ghost_label.next_to(ghost_plant, DOWN)
        
        # Network connection
        network = Line(normal_plant[0].get_bottom(), ghost_plant[0].get_bottom(), 
                      color=ORANGE, stroke_width=3)
        
        self.play(
            FadeIn(normal_plant), Write(normal_label),
            FadeIn(ghost_plant), Write(ghost_label),
            Create(network)
        )
        
        # Show carbon flow (one-way from normal to ghost)
        for _ in range(5):
            particle = Circle(radius=0.08, fill_opacity=0.9, color=YELLOW)
            particle.move_to(normal_plant[0].get_bottom())
            self.play(
                particle.animate.move_to(ghost_plant[0].get_bottom()),
                run_time=1,
                rate_func=linear
            )
            self.remove(particle)
        
        # Indian Pipe reference
        reference = Text("Monotropa (Indian Pipe)", font_size=24, color=GREY_A, slant=ITALIC)
        reference.to_edge(DOWN)
        self.play(FadeIn(reference))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, spectrum_line, mutualism_label, parasitism_label,
                                  normal_plant, normal_label, ghost_plant, ghost_label,
                                  network, reference)))
    
    def segment_10_conclusion(self):
        """Superorganism concept - 60 seconds"""
        self.camera.background_color = "#0a1a15"
        
        self.add_voiceover("10_conclusion")
        
        title = Text("Superorganism", font_size=48, weight=BOLD, color=TEAL)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create network visualization resembling neural network
        nodes = VGroup()
        positions = []
        
        # Generate random node positions
        for _ in range(20):
            x = np.random.uniform(-5, 5)
            y = np.random.uniform(-2.5, 2)
            positions.append([x, y, 0])
            node = Circle(radius=0.15, fill_opacity=0.8, color=GREEN)
            node.move_to([x, y, 0])
            nodes.add(node)
        
        # Create connections between nearby nodes
        connections = VGroup()
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                dist = np.linalg.norm(np.array(positions[i]) - np.array(positions[j]))
                if dist < 2.5:
                    line = Line(positions[i], positions[j], color=ORANGE, stroke_width=1.5)
                    connections.add(line)
        
        self.play(LaggedStart(*[FadeIn(node) for node in nodes], lag_ratio=0.05))
        self.play(LaggedStart(*[Create(conn) for conn in connections], lag_ratio=0.02), run_time=3)
        
        # Pulse animation to show "thinking"
        for _ in range(3):
            self.play(
                *[node.animate.scale(1.3).set_fill(opacity=1) for node in nodes],
                *[conn.animate.set_stroke(width=3, opacity=1) for conn in connections],
                run_time=0.4
            )
            self.play(
                *[node.animate.scale(1/1.3).set_fill(opacity=0.8) for node in nodes],
                *[conn.animate.set_stroke(width=1.5, opacity=0.6) for conn in connections],
                run_time=0.4
            )
        
        # Label
        subtitle = Text("Distributed Intelligence", font_size=32, color=TEAL)
        subtitle.to_edge(DOWN, buff=1)
        
        stat = Text("~50,000+ mycorrhizal fungal species", font_size=24, color=GREY_A)
        stat.to_edge(DOWN)
        
        self.play(Write(subtitle))
        self.wait(1)
        self.play(FadeIn(stat))
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, nodes, connections, subtitle, stat)))
    
    def segment_11_closing(self):
        """Closing message - 25 seconds"""
        self.camera.background_color = "#0a1410"
        
        self.add_voiceover("11_closing")
        
        # Create forest silhouette
        trees = VGroup()
        for i in range(7):
            x = -6 + i * 2
            height = np.random.uniform(1.5, 3)
            trunk = Rectangle(width=0.3, height=height, fill_opacity=0.6, color=YELLOW_E)
            trunk.shift([x, -2 + height/2, 0])
            canopy = Circle(radius=0.6 + np.random.uniform(-0.2, 0.3), 
                          fill_opacity=0.5, color=GREEN)
            canopy.next_to(trunk, UP, buff=0)
            trees.add(VGroup(trunk, canopy))
        
        self.play(FadeIn(trees), run_time=2)
        
        # Underground network suggestion
        network_glow = VGroup(*[
            Dot(point=[np.random.uniform(-6, 6), np.random.uniform(-3.5, -2.5), 0],
                radius=0.05, color=ORANGE)
            for _ in range(40)
        ])
        
        self.play(LaggedStart(*[FadeIn(dot) for dot in network_glow], lag_ratio=0.02))
        
        # Final message
        message = Text("An Ancient Covenant", font_size=48, color=GREEN, weight=BOLD)
        message.shift(UP * 2)
        
        self.play(Write(message), run_time=2)
        self.wait(3)
        
        # Fade to black
        everything = VGroup(trees, network_glow, message)
        self.play(FadeOut(everything), run_time=3)
        self.wait(1)
        
        # Final credits
        credits = VGroup(
            Text("THE HIDDEN NETWORK", font_size=40, weight=BOLD),
            Text("Mycorrhizal Fungi & Trees", font_size=30),
            Text("", font_size=20),
            Text("A Symbiotic Documentary", font_size=24, slant=ITALIC)
        ).arrange(DOWN, buff=0.5)
        credits.set_color_by_gradient(GREEN, YELLOW)
        
        self.play(FadeIn(credits), run_time=2)
        self.wait(3)
        self.play(FadeOut(credits), run_time=2)


# Alternative: Run segments individually for testing
class TestSegment01(Scene):
    def construct(self):
        doc = MycorrhizalDocumentary()
        doc.generate_all_audio()
        self.camera.background_color = doc.camera.background_color
        doc.segment_01_opening()


class TestSegment02(Scene):
    def construct(self):
        doc = MycorrhizalDocumentary()
        doc.generate_all_audio()
        self.camera.background_color = "#2a1a0a"
        doc.segment_02_introduction()


# Add more test classes for other segments as needed