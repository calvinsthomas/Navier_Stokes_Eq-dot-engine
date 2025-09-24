"""
Test suite for the Navier-Stokes Equation Dot Engine
"""

import unittest
import math
from dot_engine import dot, magnitude, angle_between


class TestDotEngine(unittest.TestCase):
    """Test cases for dot product and related vector operations."""
    
    def test_basic_dot_product(self):
        """Test basic dot product calculations."""
        # Test case 1: Simple integer vectors
        result = dot((1, 2), (3, 4))
        self.assertEqual(result, 11.0)
        
        # Test case 2: Float vectors
        result = dot([2.5, 3.0], [1.0, 2.0])
        self.assertEqual(result, 8.5)
        
        # Test case 3: Orthogonal vectors (should be 0)
        result = dot((1, 0), (0, 1))
        self.assertEqual(result, 0.0)
        
        # Test case 4: Parallel vectors
        result = dot((2, 3), (4, 6))
        self.assertEqual(result, 26.0)
    
    def test_dot_product_edge_cases(self):
        """Test edge cases for dot product."""
        # Zero vectors
        result = dot((0, 0), (1, 2))
        self.assertEqual(result, 0.0)
        
        result = dot((0, 0), (0, 0))
        self.assertEqual(result, 0.0)
        
        # Negative components
        result = dot((-1, -2), (3, 4))
        self.assertEqual(result, -11.0)
        
        # Mixed positive/negative
        result = dot((1, -2), (-3, 4))
        self.assertEqual(result, -11.0)
    
    def test_dot_product_validation(self):
        """Test input validation for dot product."""
        # Test wrong dimensions
        with self.assertRaises(ValueError):
            dot((1, 2, 3), (4, 5))  # 3D vs 2D
        
        with self.assertRaises(ValueError):
            dot((1,), (2, 3))  # 1D vs 2D
        
        # Test non-numeric inputs
        with self.assertRaises(TypeError):
            dot(("a", "b"), (1, 2))
        
        with self.assertRaises(TypeError):
            dot((1, 2), (None, 4))
    
    def test_vector_magnitude(self):
        """Test vector magnitude calculations."""
        # Test case 1: Classic 3-4-5 triangle
        result = magnitude((3, 4))
        self.assertEqual(result, 5.0)
        
        # Test case 2: Unit vectors
        result = magnitude((1, 0))
        self.assertEqual(result, 1.0)
        
        result = magnitude((0, 1))
        self.assertEqual(result, 1.0)
        
        # Test case 3: Zero vector
        result = magnitude((0, 0))
        self.assertEqual(result, 0.0)
        
        # Test case 4: Negative components
        result = magnitude((-3, -4))
        self.assertEqual(result, 5.0)
    
    def test_magnitude_validation(self):
        """Test input validation for magnitude."""
        with self.assertRaises(ValueError):
            magnitude((1, 2, 3))  # 3D vector
        
        with self.assertRaises(TypeError):
            magnitude(("a", "b"))  # Non-numeric
    
    def test_angle_between_vectors(self):
        """Test angle calculations between vectors."""
        # Test case 1: Orthogonal vectors (90 degrees)
        angle = angle_between((1, 0), (0, 1))
        self.assertAlmostEqual(angle, math.pi/2, places=10)
        
        # Test case 2: Parallel vectors (0 degrees)
        angle = angle_between((1, 2), (2, 4))
        self.assertAlmostEqual(angle, 0.0, places=7)
        
        # Test case 3: Opposite vectors (180 degrees)
        angle = angle_between((1, 0), (-1, 0))
        self.assertAlmostEqual(angle, math.pi, places=10)
        
        # Test case 4: 45 degree angle
        angle = angle_between((1, 0), (1, 1))
        self.assertAlmostEqual(angle, math.pi/4, places=10)
    
    def test_angle_validation(self):
        """Test input validation for angle calculations."""
        # Test zero vector
        with self.assertRaises(ValueError):
            angle_between((0, 0), (1, 2))
        
        with self.assertRaises(ValueError):
            angle_between((1, 2), (0, 0))
    
    def test_fluid_dynamics_applications(self):
        """Test scenarios relevant to Navier-Stokes equations."""
        # Velocity vector dot product (common in fluid dynamics)
        velocity1 = (2.5, 1.8)  # m/s
        velocity2 = (1.2, 3.0)  # m/s
        
        dot_product = dot(velocity1, velocity2)
        expected = 2.5 * 1.2 + 1.8 * 3.0  # 3.0 + 5.4 = 8.4
        self.assertEqual(dot_product, expected)
        
        # Pressure gradient dot product
        pressure_grad = (-0.5, -1.2)  # Pa/m
        area_normal = (1.0, 0.0)      # unit normal
        
        force_component = dot(pressure_grad, area_normal)
        self.assertEqual(force_component, -0.5)
    
    def test_performance_with_various_inputs(self):
        """Test performance and accuracy with various input types."""
        # Test with tuples
        result1 = dot((1.5, 2.5), (2.0, 3.0))
        
        # Test with lists
        result2 = dot([1.5, 2.5], [2.0, 3.0])
        
        # Should give same result
        self.assertEqual(result1, result2)
        self.assertEqual(result1, 10.5)


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)