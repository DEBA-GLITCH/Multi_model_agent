class CriticAgent:
    def review(self, plan: dict, execution_result: dict) -> dict:
        steps = plan.get("steps", [])
        actions_text = " ".join(
            step.get("action", "").lower() for step in steps
        )

        # Detect business characteristics
        is_food = any(word in actions_text for word in ["food", "restaurant", "grocery", "delivery"])
        is_online = any(word in actions_text for word in ["online", "ecommerce", "delivery", "platform"])
        has_physical = any(word in actions_text for word in ["shop", "store", "establishment"])

        # Mandatory checks
        issues = []

        # GST logic
        if is_online and "gst" not in actions_text:
            issues.append("GST registration is mandatory for online or hybrid businesses")

        # FSSAI logic
        if is_food and "fssai" not in actions_text:
            issues.append("FSSAI registration/license required for food-related businesses")

        if not is_food and "fssai" in actions_text:
            issues.append("FSSAI included for a non-food business")

        # Shops & Establishment logic
        if has_physical and "shop" not in actions_text:
            issues.append("Shops & Establishment registration required for physical businesses")

        if issues:
            return {
                "decision": "REJECT",
                "reasons": issues,
                "severity": "major",
                "required_changes": issues,
                "confidence_score": 0.4
            }

        return {
            "decision": "APPROVE",
            "reasons": [],
            "severity": "minor",
            "required_changes": [],
            "confidence_score": 0.9
        }
