copilot/fix-e087342b-608b-473e-81bf-7ea60b01ae4e
# Navier-Stokes Equation Dot Engine

A Python implementation of 2D vector dot product operations specifically designed for fluid dynamics calculations and Navier-Stokes equation computations.

## Features

- **Dot Product Calculation**: Efficient 2D vector dot product implementation
- **Vector Magnitude**: Calculate the length/magnitude of 2D vectors
- **Angle Calculation**: Compute angles between vectors in radians
- **Input Validation**: Comprehensive error handling for invalid inputs
- **Fluid Dynamics Ready**: Optimized for computational fluid dynamics applications

## Installation

Simply clone this repository:
```bash
git clone https://github.com/calvinsthomas/Navier_Stokes_Eq-dot-engine.git
cd Navier_Stokes_Eq-dot-engine
```

## Usage

### Basic Dot Product

```python
from dot_engine import dot

# Calculate dot product of two 2D vectors
result = dot((1, 2), (3, 4))  # Returns 11.0
print(f"Dot product: {result}")
```

### Vector Operations

```python
from dot_engine import dot, magnitude, angle_between
import math

# Vector operations
v1 = (3.0, 4.0)
v2 = (1.0, 2.0)

dot_product = dot(v1, v2)           # 11.0
mag_v1 = magnitude(v1)              # 5.0
angle = angle_between(v1, v2)       # Angle in radians
angle_degrees = math.degrees(angle) # Convert to degrees
```

### Fluid Dynamics Applications

```python
# Velocity field analysis
velocity = (2.5, 1.8)  # m/s
speed = magnitude(velocity)  # Calculate flow speed

# Pressure gradient force calculation
pressure_grad = (-100.0, -50.0)  # Pa/m
area_normal = (1.0, 0.0)          # Unit normal
force_component = dot(pressure_grad, area_normal)
```

## API Reference

### `dot(vector1, vector2)`
Calculate the dot product of two 2D vectors.

**Parameters:**
- `vector1` (tuple/list): First 2D vector as (x, y)
- `vector2` (tuple/list): Second 2D vector as (x, y)

**Returns:** `float` - The dot product

**Raises:**
- `ValueError`: If vectors are not 2D
- `TypeError`: If vector components are not numeric

### `magnitude(vector)`
Calculate the magnitude (length) of a 2D vector.

**Parameters:**
- `vector` (tuple/list): 2D vector as (x, y)

**Returns:** `float` - The magnitude

### `angle_between(vector1, vector2)`
Calculate the angle between two 2D vectors in radians.

**Parameters:**
- `vector1` (tuple/list): First 2D vector
- `vector2` (tuple/list): Second 2D vector

**Returns:** `float` - Angle in radians (0 to π)

## Testing

Run the comprehensive test suite:
```bash
python -m unittest test_dot_engine.py -v
```

## Examples

Run the examples to see the dot engine in action:
```bash
python examples.py
```

## Applications in Fluid Dynamics

This dot engine is particularly useful for:
- **Velocity field calculations** in computational fluid dynamics
- **Pressure gradient computations** for force analysis  
- **Flow field analysis** and visualization
- **Vector projections** in momentum equations
- **Kinetic energy calculations** in turbulence modeling

## BTSIM METHODOLOGY IP PROCESS

This implementation follows BTSIM methodology principles for numerical computation in fluid dynamics applications. 
=======
<iframe src="https://github.com/sponsors/calvinsthomas/card" title="Sponsor calvinsthomas" height="225" width="600" style="border: 0;"></iframe>
@BTSIM TEAM IP CLOSE-KNIT TEAM DEFINED MY IP PROCESSES!
main
