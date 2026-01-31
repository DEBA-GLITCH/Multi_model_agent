class PlannerAgent:
    def create_plan(self, user_input: str, feedback: list | None = None) -> dict:
        # Default values
        a, b = 2, 5  # intentionally wrong first

        # If critic gave feedback, revise the plan
        if feedback:
            if "Fix calculation logic or inputs" in feedback:
                a, b = 2, 3  # corrected values

        return {
            "goal": "Add two numbers",
            "steps": [
                {
                    "step_id": "step_1",
                    "action": "calculator.add",
                    "inputs": {"a": a, "b": b},
                    "expected_output": "Sum of a and b"
                }
            ],
            "dependencies": {},
            "success_criteria": ["Result equals 5"],
            "constraints": {}
        }
