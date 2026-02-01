class CriticAgent:
    def review(self, plan: dict, execution_result: dict) -> dict:
        steps = plan.get("steps", [])
        actions_text = " ".join(
            step.get("action", "").lower() for step in steps
        )

        # Define compliance areas with semantic keywords
        compliance_areas = {
            "registration": ["register", "incorporat", "company", "business"],
            "tax": ["gst", "tax", "pan"],
            "food": ["fssai", "food"],
            "banking": ["bank", "account"]
        }

        found = {}
        missing = []

        for area, keywords in compliance_areas.items():
            if any(keyword in actions_text for keyword in keywords):
                found[area] = True
            else:
                found[area] = False
                missing.append(area)

        score = sum(found.values())
        max_score = len(compliance_areas)
        confidence_score = round(score / max_score, 2)

        # Approval threshold
        if confidence_score >= 0.75:
            return {
                "decision": "APPROVE",
                "reasons": [],
                "severity": "minor",
                "required_changes": [],
                "confidence_score": confidence_score
            }

        # Otherwise reject with precise guidance
        return {
            "decision": "REJECT",
            "reasons": [
                f"Missing or weak compliance areas: {missing}"
            ],
            "severity": "major",
            "required_changes": [
                f"Add steps addressing: {', '.join(missing)}"
            ],
            "confidence_score": confidence_score
        }
