class PlannerAgent:
    def create_plan(self, user_input: str) -> dict:
        return {
            "goal": "Add two numbers",
            "steps": [
                {
                    "step_id": "step_1",
                    "action": "calculator.add",
                    "inputs": {"a": 4, "b": 3},
                    "expected_output": "Sum of a and b"
                }
            ],
            "dependencies": {},
            "success_criteria": ["Result equals 5"],
            "constraints": {}
        }


