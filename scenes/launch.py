from manim import *
from .common import make_starship, make_launchpad

def build_launch(scene):
    """Create the launch scene"""
    # Set up scene
    scene.set_camera_orientation(phi=75*DEGREES, theta=-30*DEGREES)
    
    # Create launchpad and starship
    pad = make_launchpad()
    ship = make_starship().move_to(pad.get_center() + UP*1.5)
    scene.add(pad, ship)
    
    # Countdown - using Text instead of Integer
    countdown = Text("10", font_size=48, color=RED).to_edge(UP)
    scene.add(countdown)
    for i in range(9, 0, -1):
        scene.play(Transform(countdown, Text(str(i), font_size=48, color=RED).to_edge(UP)), run_time=0.5)
    scene.play(FadeOut(countdown))
    
    # Launch with smoke effect
    smoke = VGroup()
    for _ in range(20):
        dot = Dot(radius=0.1, color=WHITE, fill_opacity=0.7)
        dot.move_to(ship.get_bottom())
        smoke.add(dot)
    
    scene.add(smoke)
    scene.play(
        ship.animate.shift(UP*10),
        smoke.animate.shift(DOWN*2).scale(3).set_opacity(0),
        run_time=5,
        rate_func=smooth
    )
    scene.remove(smoke)
