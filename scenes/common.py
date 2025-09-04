from manim import *
import numpy as np

def make_starship():
    """Create a simple Starship model"""
    body = Cylinder(radius=0.2, height=1, resolution=24).set_color(GRAY)
    nose = Cone(base_radius=0.2, height=0.4, resolution=24).set_color(LIGHT_GRAY)
    nose.next_to(body, UP, buff=0)
    fins = VGroup(
        Triangle().scale(0.2).rotate(PI/2).set_color(GRAY).next_to(body, DOWN+LEFT, buff=0.1),
        Triangle().scale(0.2).rotate(PI/2).set_color(GRAY).next_to(body, DOWN+RIGHT, buff=0.1)
    )
    return VGroup(body, nose, fins)

def make_launchpad():
    """Create a simple launchpad"""
    base = Square(side_length=2).set_color(DARK_GRAY).rotate(PI/2, RIGHT)
    tower = Cube(side_length=0.2).stretch(3, 2).set_color(GRAY).next_to(base, UP, buff=0)
    return VGroup(base, tower)

def make_planet(radius, color, position):
    """Create a planet"""
    return Sphere(radius=radius, resolution=24).set_color(color).move_to(position)
