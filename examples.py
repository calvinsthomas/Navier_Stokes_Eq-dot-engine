"""
Examples demonstrating the Navier-Stokes Equation Dot Engine
"""

from dot_engine import dot, magnitude, angle_between
import math


def main():
    """Run examples demonstrating the dot engine functionality."""
    print("Navier-Stokes Equation Dot Engine - Examples")
    print("=" * 50)
    
    # Example 1: Basic vector operations
    print("\n1. Basic Vector Operations:")
    print("-" * 30)
    
    v1 = (3.0, 4.0)
    v2 = (1.0, 2.0)
    
    dot_product = dot(v1, v2)
    mag_v1 = magnitude(v1)
    mag_v2 = magnitude(v2)
    angle = angle_between(v1, v2)
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print(f"Dot product: {dot_product}")
    print(f"Magnitude of v1: {mag_v1}")
    print(f"Magnitude of v2: {mag_v2}")
    print(f"Angle between vectors: {angle:.4f} radians ({math.degrees(angle):.2f}°)")
    
    # Example 2: Fluid dynamics applications
    print("\n2. Fluid Dynamics Applications:")
    print("-" * 35)
    
    # Velocity field at a point
    velocity = (2.5, 1.8)  # m/s in x and y directions
    print(f"Velocity vector: {velocity} m/s")
    print(f"Speed (magnitude): {magnitude(velocity):.2f} m/s")
    
    # Force calculation using pressure gradient
    pressure_gradient = (-100.0, -50.0)  # Pa/m
    area_normal = (1.0, 0.0)  # unit normal vector
    
    force_component = dot(pressure_gradient, area_normal)
    print(f"Pressure gradient: {pressure_gradient} Pa/m")
    print(f"Area normal: {area_normal}")
    print(f"Force component: {force_component} Pa")
    
    # Example 3: Orthogonal and parallel vectors
    print("\n3. Special Vector Relationships:")
    print("-" * 35)
    
    # Orthogonal vectors (perpendicular)
    ortho_v1 = (1.0, 0.0)
    ortho_v2 = (0.0, 1.0)
    ortho_dot = dot(ortho_v1, ortho_v2)
    ortho_angle = angle_between(ortho_v1, ortho_v2)
    
    print(f"Orthogonal vectors: {ortho_v1} and {ortho_v2}")
    print(f"Dot product (should be 0): {ortho_dot}")
    print(f"Angle (should be 90°): {math.degrees(ortho_angle):.1f}°")
    
    # Parallel vectors
    parallel_v1 = (2.0, 3.0)
    parallel_v2 = (4.0, 6.0)  # Scaled version of v1
    parallel_dot = dot(parallel_v1, parallel_v2)
    parallel_angle = angle_between(parallel_v1, parallel_v2)
    
    print(f"Parallel vectors: {parallel_v1} and {parallel_v2}")
    print(f"Dot product: {parallel_dot}")
    print(f"Angle (should be 0°): {math.degrees(parallel_angle):.6f}°")
    
    # Example 4: Flow field analysis
    print("\n4. Flow Field Analysis:")
    print("-" * 25)
    
    # Simulate velocity vectors at different points in a flow field
    flow_points = [
        ((0.0, 0.0), (1.0, 0.5)),  # Point and velocity
        ((1.0, 0.0), (0.8, 0.7)),
        ((0.0, 1.0), (0.6, 0.9)),
        ((1.0, 1.0), (0.4, 1.1))
    ]
    
    print("Flow field velocity analysis:")
    total_kinetic_energy = 0.0
    
    for i, (point, velocity) in enumerate(flow_points):
        speed = magnitude(velocity)
        # Kinetic energy per unit mass: 0.5 * v²
        kinetic_energy = 0.5 * speed**2
        total_kinetic_energy += kinetic_energy
        
        print(f"  Point {point}: velocity {velocity}, speed {speed:.3f}, KE {kinetic_energy:.3f}")
    
    print(f"Total kinetic energy per unit mass: {total_kinetic_energy:.3f}")
    
    print("\n" + "=" * 50)
    print("Examples completed successfully!")


if __name__ == "__main__":
    main()