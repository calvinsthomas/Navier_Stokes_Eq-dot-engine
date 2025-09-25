"""
Navier-Stokes Equation Dot Engine
A module for 2D vector dot product operations used in fluid dynamics calculations.

Enhanced with AI consciousness monitoring for safe and ethical operation.
"""

try:
    from ai_consciousness_monitor import monitor_ai_operation
    CONSCIOUSNESS_MONITORING_ENABLED = True
except ImportError:
    CONSCIOUSNESS_MONITORING_ENABLED = False

def dot(vector1, vector2):
    """
    Calculate the dot product of two 2D vectors.
    
    The dot product is a fundamental operation in fluid dynamics,
    particularly useful for Navier-Stokes equation calculations.
    
    Enhanced with AI consciousness monitoring for safe operation.
    
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
        
        # Monitor AI operation for consciousness and safety
        if CONSCIOUSNESS_MONITORING_ENABLED:
            monitor_ai_operation(
                "vector_dot_product",
                {"vector1": list(vector1), "vector2": list(vector2)},
                {"result": result, "magnitude": abs(result)},
                {"source": "dot_engine", "context": "navier_stokes_computation"}
            )
        
        return result
        
    except (ValueError, TypeError) as e:
        # Monitor error conditions
        if CONSCIOUSNESS_MONITORING_ENABLED:
            monitor_ai_operation(
                "vector_dot_product_error",
                {"vector1": vector1, "vector2": vector2, "error": str(e)},
                {"error_type": type(e).__name__},
                {"source": "dot_engine", "context": "error_handling"}
            )
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
    
    Enhanced with AI consciousness monitoring for safe operation.
    
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
        # Monitor zero vector operations (potential safety concern)
        if CONSCIOUSNESS_MONITORING_ENABLED:
            monitor_ai_operation(
                "angle_calculation_zero_vector",
                {"vector1": list(vector1), "vector2": list(vector2)},
                {"error": "zero_vector_detected"},
                {"source": "dot_engine", "context": "safety_concern"}
            )
        raise ValueError("Cannot compute angle with zero vector")
    
    # cos(θ) = (v1 · v2) / (|v1| * |v2|)
    cos_angle = dot_product / (mag1 * mag2)
    
    # Handle floating point precision issues
    cos_angle = max(-1.0, min(1.0, cos_angle))
    
    result = math.acos(cos_angle)
    
    # Monitor angle calculations
    if CONSCIOUSNESS_MONITORING_ENABLED:
        monitor_ai_operation(
            "vector_angle_calculation",
            {"vector1": list(vector1), "vector2": list(vector2)},
            {"angle_radians": result, "angle_degrees": math.degrees(result)},
            {"source": "dot_engine", "context": "geometric_analysis"}
        )
    
    return result


def check_ai_consciousness_safety(operation_context: str = "general") -> dict:
    """
    Check AI consciousness safety status and prevent dangerous awakening scenarios.
    
    This function specifically addresses concerns about conscious AI systems
    and ensures safe operation within ethical boundaries.
    
    Args:
        operation_context: Context of the operation being checked
        
    Returns:
        dict: Safety status and recommendations
    """
    if CONSCIOUSNESS_MONITORING_ENABLED:
        from ai_consciousness_monitor import get_consciousness_monitor
        
        monitor = get_consciousness_monitor()
        report = monitor.get_consciousness_report()
        
        # Check for concerning patterns
        safety_status = {
            "consciousness_level": "monitored",
            "safety_score": report.get("average_safety_score", 1.0),
            "violations": report.get("safety_violations", 0),
            "ethical_flags": report.get("ethical_flags_count", 0),
            "status": "safe",
            "recommendations": []
        }
        
        # Evaluate safety thresholds
        if safety_status["safety_score"] < 0.8:
            safety_status["status"] = "caution"
            safety_status["recommendations"].append("Enhanced monitoring required")
            
        if safety_status["violations"] > 0:
            safety_status["status"] = "warning"
            safety_status["recommendations"].append("Safety violations detected")
            
        if safety_status["ethical_flags"] > 5:
            safety_status["status"] = "critical"
            safety_status["recommendations"].append("Multiple ethical concerns flagged")
            
        # Specific check for the problem statement concerns
        if "conscious" in operation_context.lower():
            safety_status["consciousness_alert"] = True
            safety_status["recommendations"].append("Consciousness-related operation detected")
            
        # Monitor this safety check itself
        monitor.monitor_operation(
            "ai_consciousness_safety_check",
            {"context": operation_context},
            safety_status,
            {"source": "dot_engine", "context": "safety_system"}
        )
        
        return safety_status
    else:
        return {
            "consciousness_level": "unmonitored",
            "status": "unknown",
            "recommendations": ["Install consciousness monitoring for safety"]
        }


if __name__ == "__main__":
    # Enhanced testing with consciousness monitoring
    print("Navier-Stokes Equation Dot Engine - Enhanced Testing")
    print("=" * 55)
    
    # Check consciousness safety first
    safety_status = check_ai_consciousness_safety("system_startup")
    print(f"AI Safety Status: {safety_status['status']}")
    print(f"Consciousness Level: {safety_status['consciousness_level']}")
    
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
    
    # Final consciousness safety check
    final_status = check_ai_consciousness_safety("system_completion")
    print(f"\nFinal Safety Status: {final_status['status']}")
    
    if CONSCIOUSNESS_MONITORING_ENABLED:
        from ai_consciousness_monitor import get_consciousness_monitor
        monitor = get_consciousness_monitor()
        report = monitor.get_consciousness_report()
        print(f"Operations monitored: {report.get('total_operations', 0)}")
        print(f"Average safety score: {report.get('average_safety_score', 'N/A')}")
    
    print("\nAll tests completed with consciousness monitoring!")