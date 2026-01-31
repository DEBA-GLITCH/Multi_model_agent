class ExecutorAgent:
    def execute(self, plan: dict) -> dict:
        results = {}

        for step in plan["steps"]:
            if step["action"] == "calculator.add":
                a = step["inputs"]["a"]
                b = step["inputs"]["b"]
                results[step["step_id"]] = a + b

        return results
