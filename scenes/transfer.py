from manim import *
from .common import make_starship, make_planet

def build_transfer(scene):
    """Create the Earth to Mars transfer scene"""
    scene.set_camera_orientation(phi=75*DEGREES, theta=-30*DEGREES)
    
    # Create Earth and Mars
    earth = make_planet(1, BLUE, LEFT*5)
    mars = make_planet(0.7, RED, RIGHT*5)
    scene.add(earth, mars)
    
    # Create transfer trajectory
    trajectory = ParametricFunction(
        lambda t: np.array([
            5 * np.cos(t) - 2.5,
            2 * np.sin(t),
            0
        ]),
        t_range=[0, PI],
        color=WHITE
    )
    scene.add(trajectory)
    
    # Animate ship along trajectory
    ship = make_starship().move_to(trajectory.get_start())
    scene.add(ship)
    
    # Animate along path
    for t in np.linspace(0, 1, 100):
        point = trajectory.point_from_proportion(t)
        scene.play(
            ship.animate.move_to(point),
            run_time=0.05,
            rate_func=linear
        )
