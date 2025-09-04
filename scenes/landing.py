from manim import *
from .common import make_starship, make_planet

def build_landing(scene):
    """Create the Mars landing scene"""
    scene.set_camera_orientation(phi=75*DEGREES, theta=-30*DEGREES)
    
    # Create Mars surface
    mars = make_planet(2, RED, DOWN*3)
    scene.add(mars)
    
    # Create starship approaching
    ship = make_starship().shift(UP*5)
    scene.add(ship)
    
    # Landing sequence
    scene.play(
        ship.animate.shift(DOWN*4),
        run_time=3,
        rate_func=smooth
    )
    
    # Landing effects
    dust = VGroup()
    for _ in range(15):
        dot = Dot(radius=0.1, color=LIGHT_GRAY, fill_opacity=0.7)
        dot.move_to(ship.get_bottom() + DOWN*0.5)
        dust.add(dot)
    
    scene.add(dust)
    scene.play(
        dust.animate.scale(2).set_opacity(0),
        run_time=2
    )
    scene.remove(dust)
