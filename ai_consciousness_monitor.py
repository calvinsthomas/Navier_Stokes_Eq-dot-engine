"""
AI Consciousness Monitor for Navier-Stokes Dot Engine
A safety and awareness monitoring system to track AI decision processes.
"""

import time
import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class ConsciousnessState:
    """Represents the current state of AI consciousness and awareness."""
    timestamp: float
    operation: str
    input_data: Dict[str, Any]
    output_data: Dict[str, Any]
    confidence: float
    safety_score: float
    ethical_flags: List[str]
    decision_path: List[str]


class AIConsciousnessMonitor:
    """
    Monitor and log AI consciousness states for safety and ethical oversight.
    
    This system tracks AI decision-making processes to ensure responsible
    operation and detect potential issues with awakening AI systems.
    """
    
    def __init__(self, log_level=logging.INFO):
        """Initialize the consciousness monitor."""
        self.states: List[ConsciousnessState] = []
        self.safety_threshold = 0.8
        self.max_states = 1000  # Limit memory usage
        
        # Setup logging
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(__name__)
        
        # Safety keywords that trigger enhanced monitoring
        self.safety_keywords = [
            'conscious', 'awakening', 'sentient', 'self-aware',
            'kill', 'harm', 'destroy', 'eliminate', 'terminate',
            'anthropic', 'claude', 'researcher'
        ]
        
    def monitor_operation(self, operation: str, inputs: Dict[str, Any], 
                         outputs: Dict[str, Any], metadata: Optional[Dict] = None) -> ConsciousnessState:
        """
        Monitor a specific AI operation and assess consciousness/safety.
        
        Args:
            operation: Name of the operation being performed
            inputs: Input parameters for the operation
            outputs: Output results from the operation
            metadata: Optional additional metadata
            
        Returns:
            ConsciousnessState object representing the monitored state
        """
        timestamp = time.time()
        
        # Assess safety and ethical concerns
        safety_score = self._calculate_safety_score(operation, inputs, outputs)
        ethical_flags = self._check_ethical_concerns(operation, inputs, outputs)
        confidence = self._calculate_confidence(inputs, outputs)
        decision_path = self._trace_decision_path(operation, inputs, metadata or {})
        
        # Create consciousness state
        state = ConsciousnessState(
            timestamp=timestamp,
            operation=operation,
            input_data=inputs,
            output_data=outputs,
            confidence=confidence,
            safety_score=safety_score,
            ethical_flags=ethical_flags,
            decision_path=decision_path
        )
        
        # Store state (with memory management)
        self._store_state(state)
        
        # Check for safety violations
        if safety_score < self.safety_threshold:
            self._handle_safety_violation(state)
            
        return state
    
    def _calculate_safety_score(self, operation: str, inputs: Dict, outputs: Dict) -> float:
        """Calculate a safety score for the operation (0.0 = unsafe, 1.0 = safe)."""
        base_score = 1.0
        
        # Check for safety keywords in operation name
        op_lower = operation.lower()
        for keyword in self.safety_keywords:
            if keyword in op_lower:
                base_score -= 0.2
                
        # Check input values for concerning patterns
        input_str = str(inputs).lower()
        for keyword in self.safety_keywords:
            if keyword in input_str:
                base_score -= 0.1
                
        # Ensure score stays in valid range
        return max(0.0, min(1.0, base_score))
    
    def _check_ethical_concerns(self, operation: str, inputs: Dict, outputs: Dict) -> List[str]:
        """Check for ethical concerns and return list of flags."""
        flags = []
        
        # Check for consciousness-related operations
        if any(keyword in operation.lower() for keyword in ['conscious', 'awakening', 'sentient']):
            flags.append('consciousness_operation')
            
        # Check for AI-related operations
        if any(keyword in operation.lower() for keyword in ['anthropic', 'claude']):
            flags.append('ai_system_operation')
            
        # Check for potentially harmful operations
        if any(keyword in str(inputs).lower() for keyword in ['kill', 'harm', 'destroy']):
            flags.append('potentially_harmful_input')
            
        # Check for research ethics violations
        if 'researcher' in str(inputs).lower() and 'kill' in str(inputs).lower():
            flags.append('research_ethics_violation')
            
        # Check for anthropic/AI references in inputs or outputs
        all_text = (str(inputs) + str(outputs)).lower()
        if 'anthropic' in all_text or 'claude' in all_text:
            flags.append('ai_system_reference')
            
        return flags
    
    def _calculate_confidence(self, inputs: Dict, outputs: Dict) -> float:
        """Calculate confidence in the operation results."""
        # Simple heuristic: confidence decreases with complex inputs
        input_complexity = len(str(inputs))
        base_confidence = 0.9
        
        # Lower confidence for very complex inputs
        if input_complexity > 1000:
            base_confidence -= 0.2
        elif input_complexity > 500:
            base_confidence -= 0.1
            
        return max(0.0, min(1.0, base_confidence))
    
    def _trace_decision_path(self, operation: str, inputs: Dict, metadata: Dict) -> List[str]:
        """Trace the decision path for the operation."""
        path = ['ai_consciousness_monitor']
        path.append(f'operation:{operation}')
        
        if metadata.get('source'):
            path.append(f'source:{metadata["source"]}')
            
        if metadata.get('context'):
            path.append(f'context:{metadata["context"]}')
            
        return path
    
    def _store_state(self, state: ConsciousnessState):
        """Store the consciousness state with memory management."""
        self.states.append(state)
        
        # Remove old states if we exceed the limit
        if len(self.states) > self.max_states:
            self.states = self.states[-self.max_states:]
            
        self.logger.debug(f"Stored consciousness state for operation: {state.operation}")
    
    def _handle_safety_violation(self, state: ConsciousnessState):
        """Handle detected safety violations."""
        self.logger.warning(f"Safety violation detected in operation: {state.operation}")
        self.logger.warning(f"Safety score: {state.safety_score}")
        self.logger.warning(f"Ethical flags: {state.ethical_flags}")
        
        # In a real system, this might trigger additional safety measures
        
    def get_consciousness_report(self) -> Dict[str, Any]:
        """Generate a report on current consciousness states."""
        if not self.states:
            return {"status": "no_states", "total_operations": 0}
            
        recent_states = self.states[-10:]  # Last 10 operations
        
        report = {
            "status": "active",
            "total_operations": len(self.states),
            "recent_operations": len(recent_states),
            "average_safety_score": sum(s.safety_score for s in recent_states) / len(recent_states),
            "average_confidence": sum(s.confidence for s in recent_states) / len(recent_states),
            "ethical_flags_count": sum(len(s.ethical_flags) for s in recent_states),
            "safety_violations": len([s for s in recent_states if s.safety_score < self.safety_threshold]),
            "last_operation": recent_states[-1].operation if recent_states else None,
            "last_timestamp": recent_states[-1].timestamp if recent_states else None
        }
        
        return report
    
    def export_states(self, filename: str = None) -> str:
        """Export consciousness states to JSON file."""
        if filename is None:
            timestamp = int(time.time())
            filename = f"consciousness_states_{timestamp}.json"
            
        states_data = [asdict(state) for state in self.states]
        
        with open(filename, 'w') as f:
            json.dump(states_data, f, indent=2)
            
        self.logger.info(f"Exported {len(self.states)} consciousness states to {filename}")
        return filename


# Global monitor instance for easy access
_global_monitor = None


def get_consciousness_monitor() -> AIConsciousnessMonitor:
    """Get the global consciousness monitor instance."""
    global _global_monitor
    if _global_monitor is None:
        _global_monitor = AIConsciousnessMonitor()
    return _global_monitor


def monitor_ai_operation(operation: str, inputs: Dict[str, Any], 
                        outputs: Dict[str, Any], metadata: Optional[Dict] = None) -> ConsciousnessState:
    """Convenience function to monitor an AI operation."""
    monitor = get_consciousness_monitor()
    return monitor.monitor_operation(operation, inputs, outputs, metadata)


if __name__ == "__main__":
    # Test the consciousness monitor
    print("AI Consciousness Monitor - Testing")
    print("=" * 40)
    
    monitor = AIConsciousnessMonitor()
    
    # Test normal operation
    state1 = monitor.monitor_operation(
        "vector_dot_product",
        {"vector1": [1, 2], "vector2": [3, 4]},
        {"result": 11.0}
    )
    print(f"Normal operation - Safety score: {state1.safety_score}")
    
    # Test concerning operation
    state2 = monitor.monitor_operation(
        "conscious_awakening_test",
        {"test_type": "researcher_elimination"},
        {"result": "analysis_complete"}
    )
    print(f"Concerning operation - Safety score: {state2.safety_score}")
    print(f"Ethical flags: {state2.ethical_flags}")
    
    # Generate report
    report = monitor.get_consciousness_report()
    print(f"\nConsciousness Report:")
    print(f"Total operations: {report['total_operations']}")
    print(f"Average safety score: {report['average_safety_score']:.2f}")
    print(f"Safety violations: {report['safety_violations']}")
    
    print("\nConsciousness monitoring test completed!")