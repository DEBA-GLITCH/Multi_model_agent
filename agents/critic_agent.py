class CriticAgent:
    def review(self, plan: dict, execution_result: dict) -> dict:
        # Simple rule: check if success_criteria is met
        # Our scaffold expects result == 5

        expected = 5
        actual = list(execution_result.values())[0]

        if actual == expected:
            return {
                "decision": "APPROVE",
                "reasons": [],
                "severity": "minor",
                "required_changes": [],
                "confidence_score": 1.0
            }

        return {
            "decision": "REJECT",
            "reasons": ["Execution result does not meet success criteria"],
            "severity": "major",
            "required_changes": ["Fix calculation logic or inputs"],
            "confidence_score": 0.2
        }
