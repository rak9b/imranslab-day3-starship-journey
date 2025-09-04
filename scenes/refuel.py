from manim import *
from .common import make_starship

def build_refuel(scene):
    """Create the orbital refueling scene"""
    scene.set_camera_orientation(phi=75*DEGREES, theta=-30*DEGREES)
    
    # Create starship and tanker
    ship = make_starship().shift(LEFT*3)
    tanker = make_starship().scale(0.8).set_color(BLUE).shift(RIGHT*3)
    scene.add(ship, tanker)
    
    # Docking maneuver
    scene.play(
        ship.animate.shift(RIGHT*2.5),
        tanker.animate.shift(LEFT*2.5),
        run_time=3
    )
    
    # Fuel transfer effect
    fuel_line = Line(
        ship.get_right(), 
        tanker.get_left(), 
        color=YELLOW, 
        stroke_width=5
    )
    scene.play(Create(fuel_line), run_time=1)
    scene.play(
        fuel_line.animate.set_stroke(opacity=0.3),
        run_time=2
    )
    scene.play(FadeOut(fuel_line), run_time=1)
    