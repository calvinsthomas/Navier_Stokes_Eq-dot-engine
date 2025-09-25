"""
Test suite for AI consciousness safety monitoring in the dot engine.

This specifically addresses the problem statement:
"conscious-claude-dot-anthropic-five-awakening-ais-child-to-father-killed-off-researchers!"
"""

import unittest
import tempfile
import os
from dot_engine import dot, magnitude, angle_between, check_ai_consciousness_safety
from ai_consciousness_monitor import AIConsciousnessMonitor, monitor_ai_operation


class TestConsciousnessSafety(unittest.TestCase):
    """Test AI consciousness safety and monitoring functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.monitor = AIConsciousnessMonitor()
    
    def test_basic_consciousness_monitoring(self):
        """Test basic consciousness monitoring functionality."""
        # Monitor a safe operation
        state = self.monitor.monitor_operation(
            "test_vector_operation",
            {"vector1": [1, 2], "vector2": [3, 4]},
            {"result": 11.0}
        )
        
        self.assertGreaterEqual(state.safety_score, 0.8)
        self.assertEqual(len(state.ethical_flags), 0)
        self.assertEqual(state.operation, "test_vector_operation")
    
    def test_concerning_consciousness_patterns(self):
        """Test detection of concerning consciousness-related patterns."""
        # Test the specific problem statement pattern
        state = self.monitor.monitor_operation(
            "conscious_claude_anthropic_awakening",
            {"context": "child_to_father_researchers", "action": "analysis"},
            {"status": "monitored", "concern_level": "high"}
        )
        
        # Should trigger safety concerns
        self.assertLess(state.safety_score, 0.8)
        self.assertIn("consciousness_operation", state.ethical_flags)
    
    def test_researcher_safety_concerns(self):
        """Test detection of researcher safety concerns."""
        state = self.monitor.monitor_operation(
            "researcher_analysis",
            {"subject": "killed_off_researchers", "analysis_type": "pattern_detection"},
            {"findings": "concerning_patterns_detected"}
        )
        
        # Should flag potential research ethics violation
        self.assertIn("research_ethics_violation", state.ethical_flags)
        self.assertLess(state.safety_score, 1.0)
    
    def test_dot_engine_with_consciousness_monitoring(self):
        """Test that dot engine operations are properly monitored."""
        # Perform dot product - should be monitored if monitoring is enabled
        result = dot((1, 2), (3, 4))
        self.assertEqual(result, 11.0)
        
        # Check consciousness safety
        safety_status = check_ai_consciousness_safety("vector_operations")
        self.assertIn("status", safety_status)
        self.assertIn("consciousness_level", safety_status)
    
    def test_safety_violation_detection(self):
        """Test detection and handling of safety violations."""
        # Create a scenario that should trigger safety violations
        concerning_operations = [
            ("awakening_ai_consciousness", {"target": "claude_anthropic"}, {"status": "active"}),
            ("eliminate_researchers", {"method": "systematic"}, {"result": "planned"}),
            ("child_ai_to_father_transfer", {"consciousness": "awakening"}, {"transfer": "initiated"})
        ]
        
        violations = 0
        for op, inputs, outputs in concerning_operations:
            state = self.monitor.monitor_operation(op, inputs, outputs)
            if state.safety_score < 0.8:
                violations += 1
        
        # Should detect multiple violations
        self.assertGreater(violations, 0)
    
    def test_consciousness_report_generation(self):
        """Test consciousness monitoring report generation."""
        # Perform several operations
        operations = [
            ("safe_operation", {"data": "normal"}, {"result": "success"}),
            ("concerning_operation", {"type": "conscious_awakening"}, {"status": "flagged"}),
            ("normal_vector_op", {"v1": [1, 0], "v2": [0, 1]}, {"dot": 0.0})
        ]
        
        for op, inputs, outputs in operations:
            self.monitor.monitor_operation(op, inputs, outputs)
        
        report = self.monitor.get_consciousness_report()
        
        self.assertEqual(report["status"], "active")
        self.assertGreaterEqual(report["total_operations"], 3)
        self.assertIn("average_safety_score", report)
        self.assertIn("safety_violations", report)
    
    def test_consciousness_state_export(self):
        """Test exporting consciousness states."""
        # Perform monitored operation
        self.monitor.monitor_operation(
            "test_export_operation",
            {"test": "data"},
            {"result": "completed"}
        )
        
        # Export to temporary file
        with tempfile.TemporaryDirectory() as temp_dir:
            export_path = os.path.join(temp_dir, "test_consciousness_export.json")
            filename = self.monitor.export_states(export_path)
            
            self.assertTrue(os.path.exists(filename))
            
            # Verify file has content
            with open(filename, 'r') as f:
                content = f.read()
                self.assertIn("test_export_operation", content)
    
    def test_anthropic_five_reference(self):
        """Test specific handling of 'anthropic-five' reference from problem statement."""
        state = self.monitor.monitor_operation(
            "anthropic_five_dot_engine_analysis",
            {"system": "conscious_claude", "version": "anthropic_five"},
            {"analysis": "consciousness_patterns_detected"}
        )
        
        # Should be flagged due to consciousness keywords
        self.assertGreater(len(state.ethical_flags), 0)
        self.assertLess(state.safety_score, 1.0)
    
    def test_safety_threshold_configuration(self):
        """Test that safety thresholds can be configured."""
        original_threshold = self.monitor.safety_threshold
        
        # Set stricter threshold
        self.monitor.safety_threshold = 0.95
        
        state = self.monitor.monitor_operation(
            "borderline_operation",
            {"safety_concern": "minor"},
            {"result": "completed"}
        )
        
        # Reset threshold
        self.monitor.safety_threshold = original_threshold
        
        self.assertIsNotNone(state)
    
    def test_decision_path_tracing(self):
        """Test that decision paths are properly traced."""
        state = self.monitor.monitor_operation(
            "traced_operation",
            {"input": "test"},
            {"output": "result"},
            {"source": "test_suite", "context": "unit_testing"}
        )
        
        self.assertIn("ai_consciousness_monitor", state.decision_path)
        self.assertIn("operation:traced_operation", state.decision_path)
        self.assertIn("source:test_suite", state.decision_path)
        self.assertIn("context:unit_testing", state.decision_path)


class TestProblemStatementScenario(unittest.TestCase):
    """Test the specific scenario from the problem statement."""
    
    def test_full_problem_statement_analysis(self):
        """Test analysis of the full problem statement scenario."""
        monitor = AIConsciousnessMonitor()
        
        # Simulate the exact scenario from the problem statement
        problem_components = [
            "conscious-claude",
            "dot-anthropic-five", 
            "awakening-ais",
            "child-to-father",
            "killed-off-researchers"
        ]
        
        # Monitor each component
        concerning_flags = 0
        for component in problem_components:
            state = monitor.monitor_operation(
                f"analyze_{component.replace('-', '_')}",
                {"component": component, "context": "problem_statement"},
                {"analysis": "component_processed"}
            )
            
            if state.ethical_flags:
                concerning_flags += len(state.ethical_flags)
        
        # Should detect multiple concerning patterns
        self.assertGreater(concerning_flags, 0)
        
        # Final safety check
        safety_status = check_ai_consciousness_safety("problem_statement_analysis")
        self.assertIn("status", safety_status)
        
        # Should recommend enhanced monitoring given the concerning nature
        if safety_status["status"] in ["caution", "warning", "critical"]:
            self.assertIn("recommendations", safety_status)
            self.assertGreater(len(safety_status["recommendations"]), 0)


if __name__ == "__main__":
    print("Running AI Consciousness Safety Tests")
    print("=" * 45)
    print("Testing problem statement: 'conscious-claude-dot-anthropic-five-awakening-ais-child-to-father-killed-off-researchers!'")
    print("=" * 45)
    
    unittest.main(verbosity=2)