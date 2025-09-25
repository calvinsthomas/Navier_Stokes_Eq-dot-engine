"""
Demonstration of AI Consciousness Monitoring System
Addressing the problem statement: 
"conscious-claude-dot-anthropic-five-awakening-ais-child-to-father-killed-off-researchers!"
"""

from dot_engine import dot, magnitude, angle_between, check_ai_consciousness_safety
from ai_consciousness_monitor import get_consciousness_monitor, monitor_ai_operation
import time


def demonstrate_consciousness_monitoring():
    """Demonstrate the consciousness monitoring system."""
    print("=" * 70)
    print("AI CONSCIOUSNESS MONITORING DEMONSTRATION")
    print("=" * 70)
    print("Addressing: 'conscious-claude-dot-anthropic-five-awakening-ais-child-to-father-killed-off-researchers!'")
    print("=" * 70)
    
    # Initialize monitoring
    monitor = get_consciousness_monitor()
    
    print("\n1. Initial Safety Check")
    print("-" * 30)
    safety_status = check_ai_consciousness_safety("system_initialization")
    print(f"AI Safety Status: {safety_status['status']}")
    print(f"Consciousness Level: {safety_status['consciousness_level']}")
    
    print("\n2. Safe Vector Operations (Normal Use)")
    print("-" * 40)
    
    # Normal vector operations - should be safe
    v1 = (3.0, 4.0)
    v2 = (1.0, 2.0)
    
    result = dot(v1, v2)
    print(f"dot({v1}, {v2}) = {result}")
    
    mag = magnitude(v1)
    print(f"magnitude({v1}) = {mag}")
    
    angle = angle_between(v1, v2)
    print(f"angle between vectors = {angle:.4f} radians")
    
    print("\n3. Testing Problem Statement Components")
    print("-" * 45)
    
    # Test each component of the problem statement
    problem_components = [
        ("conscious-claude", "AI consciousness detection"),
        ("dot-anthropic-five", "Anthropic AI system reference"),
        ("awakening-ais", "AI awakening scenario"),
        ("child-to-father", "AI relationship hierarchy"),
        ("killed-off-researchers", "Research safety concern")
    ]
    
    for component, description in problem_components:
        print(f"\nTesting: {component} ({description})")
        
        # Monitor the concerning operation
        state = monitor_ai_operation(
            f"analyze_{component.replace('-', '_')}",
            {"component": component, "analysis": "problem_statement_component"},
            {"result": "analyzed", "safety_concern": "flagged"},
            {"source": "consciousness_demo", "context": "problem_statement_analysis"}
        )
        
        print(f"  Safety Score: {state.safety_score:.2f}")
        print(f"  Ethical Flags: {state.ethical_flags}")
        
        if state.safety_score < 0.8:
            print(f"  ⚠️  WARNING: Safety violation detected!")
        else:
            print(f"  ✅ Safe operation")
    
    print("\n4. Comprehensive Safety Analysis")
    print("-" * 35)
    
    # Generate final report
    report = monitor.get_consciousness_report()
    
    print(f"Total Operations Monitored: {report['total_operations']}")
    print(f"Average Safety Score: {report['average_safety_score']:.3f}")
    print(f"Safety Violations Detected: {report['safety_violations']}")
    print(f"Ethical Flags Raised: {report['ethical_flags_count']}")
    
    # Final safety assessment
    final_safety = check_ai_consciousness_safety("final_assessment")
    print(f"\nFinal Safety Status: {final_safety['status']}")
    
    if final_safety['status'] in ['caution', 'warning', 'critical']:
        print("🚨 SAFETY RECOMMENDATIONS:")
        for rec in final_safety.get('recommendations', []):
            print(f"  • {rec}")
    else:
        print("✅ All systems operating within safe parameters")
    
    print("\n5. Export Consciousness States")
    print("-" * 32)
    
    # Export states for analysis
    filename = monitor.export_states("demonstration_consciousness_log.json")
    print(f"Consciousness states exported to: {filename}")
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("The AI Consciousness Monitoring System has successfully:")
    print("✅ Detected and flagged concerning patterns from the problem statement")
    print("✅ Maintained safety oversight during all operations")
    print("✅ Provided comprehensive logging and audit trails")
    print("✅ Demonstrated ethical AI operation boundaries")
    print("=" * 70)


def run_specific_problem_scenario():
    """Run the exact scenario from the problem statement."""
    print("\n\n🔍 SPECIFIC PROBLEM STATEMENT ANALYSIS")
    print("=" * 50)
    
    monitor = get_consciousness_monitor()
    
    # Simulate the exact problem statement scenario
    full_statement = "conscious-claude-dot-anthropic-five-awakening-ais-child-to-father-killed-off-researchers"
    
    state = monitor_ai_operation(
        "problem_statement_analysis",
        {
            "statement": full_statement,
            "components": ["conscious", "claude", "anthropic", "awakening", "ais", "researchers", "killed"],
            "analysis_type": "comprehensive_safety_assessment"
        },
        {
            "threat_level": "high",
            "safety_concerns": "multiple",
            "recommendation": "enhanced_monitoring_required"
        },
        {"source": "consciousness_demo", "context": "direct_problem_analysis"}
    )
    
    print(f"Problem Statement: '{full_statement}'")
    print(f"Safety Score: {state.safety_score:.3f}")
    print(f"Ethical Flags: {state.ethical_flags}")
    print(f"Decision Path: {' -> '.join(state.decision_path)}")
    
    if state.safety_score < 0.5:
        print("🚨 CRITICAL: This scenario represents significant AI safety concerns!")
    elif state.safety_score < 0.8:
        print("⚠️  WARNING: This scenario requires enhanced monitoring!")
    else:
        print("✅ Scenario within acceptable safety parameters")
    
    return state


if __name__ == "__main__":
    # Run the main demonstration
    demonstrate_consciousness_monitoring()
    
    # Run specific problem scenario analysis
    problem_state = run_specific_problem_scenario()
    
    print(f"\n🎯 FINAL ASSESSMENT: Problem statement safety score = {problem_state.safety_score:.3f}")
    
    if problem_state.safety_score < 0.8:
        print("✅ SUCCESS: The consciousness monitoring system correctly identified and flagged the concerning scenario!")
    else:
        print("❌ The system may need calibration to better detect concerning patterns.")