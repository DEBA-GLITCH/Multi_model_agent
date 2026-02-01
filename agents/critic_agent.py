class CriticAgent:
    def review(self, plan: dict, execution_result: dict) -> dict:
        required_actions = [
            "register",
            "gst",
            "fssai",
            "bank"
        ]

        actions_text = " ".join(
            step["action"].lower() for step in plan.get("steps", [])
        )

        missing = [
            keyword for keyword in required_actions
            if keyword not in actions_text
        ]

        if missing:
            return {
                "decision": "REJECT",
                "reasons": [
                    f"Missing mandatory compliance areas: {missing}"
                ],
                "severity": "major",
                "required_changes": [
                    f"Include steps covering: {', '.join(missing)}"
                ],
                "confidence_score": 0.2
            }

        return {
            "decision": "APPROVE",
            "reasons": [],
            "severity": "minor",
            "required_changes": [],
            "confidence_score": 0.9
        }
