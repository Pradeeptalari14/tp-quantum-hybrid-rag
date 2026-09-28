from manim import *

class QuantumKernelAnimation(Scene):
    def construct(self):
        title = Text("Quantum Kernel Feature Map in Hilbert Space", font_size=30, color=INDIGO)
        title.to_edge(UP)
        self.play(Write(title))

        classical_pt = Dot(LEFT * 3, color=BLUE, radius=0.15)
        pt_label = Text("Classical Vector", font_size=16).next_to(classical_pt, DOWN)

        sphere = Circle(radius=1.5, color=CYAN).shift(RIGHT * 3)
        sphere_label = Text("Hilbert Space\n|ψ(x)⟩", font_size=16).move_to(sphere)

        arrow = CurvedArrow(classical_pt.get_right(), sphere.get_left(), color=YELLOW)
        arrow_lbl = Text("Feature Map U(x)", font_size=14).next_to(arrow, UP)

        self.play(FadeIn(classical_pt), Write(pt_label))
        self.play(Create(arrow), Write(arrow_lbl))
        self.play(Create(sphere), Write(sphere_label))
        self.wait(1)
