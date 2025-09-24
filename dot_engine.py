"""
Navier-Stokes Equation Dot Engine
A module for 2D vector dot product operations used in fluid dynamics calculations.
"""

def dot(vector1, vector2):
    """
    Calculate the dot product of two 2D vectors.
    
    The dot product is a fundamental operation in fluid dynamics,
    particularly useful for Navier-Stokes equation calculations.
    
    Args:
        vector1 (tuple or list): First 2D vector as (x, y)
        vector2 (tuple or list): Second 2D vector as (x, y)
    
    Returns:
        float: The dot product of the two vectors
    
    Raises:
        ValueError: If vectors are not 2D (don't have exactly 2 components)
        TypeError: If vector components are not numeric
    
    Example:
        >>> dot((1, 2), (3, 4))
        11.0
        >>> dot([2.5, 3.0], [1.0, 2.0])
        8.5
    """
    # Validate input vectors
    if len(vector1) != 2 or len(vector2) != 2:
        raise ValueError("Both vectors must be 2D (have exactly 2 components)")
    
    try:
        # Extract components
        x1, y1 = float(vector1[0]), float(vector1[1])
        x2, y2 = float(vector2[0]), float(vector2[1])
        
        # Calculate dot product: v1 · v2 = x1*x2 + y1*y2
        result = x1 * x2 + y1 * y2
        return result
        
    except (ValueError, TypeError) as e:
        raise TypeError("Vector components must be numeric") from e


def magnitude(vector):
    """
    Calculate the magnitude (length) of a 2D vector.
    
    Args:
        vector (tuple or list): 2D vector as (x, y)
    
    Returns:
        float: The magnitude of the vector
    
    Example:
        >>> magnitude((3, 4))
        5.0
    """
    if len(vector) != 2:
        raise ValueError("Vector must be 2D (have exactly 2 components)")
    
    try:
        x, y = float(vector[0]), float(vector[1])
        return (x**2 + y**2)**0.5
    except (ValueError, TypeError) as e:
        raise TypeError("Vector components must be numeric") from e


def angle_between(vector1, vector2):
    """
    Calculate the angle between two 2D vectors in radians.
    
    Args:
        vector1 (tuple or list): First 2D vector as (x, y)
        vector2 (tuple or list): Second 2D vector as (x, y)
    
    Returns:
        float: Angle between vectors in radians (0 to π)
    
    Example:
        >>> import math
        >>> angle_between((1, 0), (0, 1))  # 90 degrees
        1.5707963267948966
    """
    import math
    
    dot_product = dot(vector1, vector2)
    mag1 = magnitude(vector1)
    mag2 = magnitude(vector2)
    
    if mag1 == 0 or mag2 == 0:
        raise ValueError("Cannot compute angle with zero vector")
    
    # cos(θ) = (v1 · v2) / (|v1| * |v2|)
    cos_angle = dot_product / (mag1 * mag2)
    
    # Handle floating point precision issues
    cos_angle = max(-1.0, min(1.0, cos_angle))
    
    return math.acos(cos_angle)


if __name__ == "__main__":
    # Basic testing
    print("Navier-Stokes Equation Dot Engine - Testing")
    print("=" * 45)
    
    # Test case 1: Basic dot product
    v1 = (1, 2)
    v2 = (3, 4)
    result = dot(v1, v2)
    print(f"dot({v1}, {v2}) = {result}")
    
    # Test case 2: Orthogonal vectors
    v3 = (1, 0)
    v4 = (0, 1)
    result2 = dot(v3, v4)
    print(f"dot({v3}, {v4}) = {result2}")
    
    # Test case 3: Vector magnitude
    mag = magnitude((3, 4))
    print(f"magnitude((3, 4)) = {mag}")
    
    # Test case 4: Angle between vectors
    import math
    angle = angle_between((1, 0), (0, 1))
    print(f"angle_between((1, 0), (0, 1)) = {angle} radians = {math.degrees(angle)} degrees")
    
    print("\nAll basic tests completed successfully!")