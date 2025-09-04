from manim import *
from scenes.launch import build_launch
from scenes.refuel import build_refuel
from scenes.transfer import build_transfer
from scenes.landing import build_landing

class StarshipJourney(ThreeDScene):
    def construct(self):
        # Title screen - using Text instead of Tex
        title = Text("Starship Journey: Earth to Mars", font_size=36)
        subtitle = Text("ImransLab Day 3 Assignment", font_size=24)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Run all scenes
        build_launch(self)
        self.wait(1)
        
        build_refuel(self)
        self.wait(1)
        
        build_transfer(self)
        self.wait(1)
        
        build_landing(self)
        self.wait(2)
        
        # End screen
        end_text = Text("Mission Accomplished!", font_size=36)
        self.play(Write(end_text))
        self.wait(3)
