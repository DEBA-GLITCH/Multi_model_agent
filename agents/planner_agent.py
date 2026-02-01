import json
import os
from groq import Groq

from config.settings import GROQ_MODEL


class PlannerAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def _load_prompt(self) -> str:
        with open("prompts/planner.txt", "r") as f:
            return f.read()

    def create_plan(self, user_input: str, feedback: list | None = None) -> dict:
        system_prompt = self._load_prompt()

        user_prompt = f"""
Startup idea:
{user_input}
"""

        if feedback:
            user_prompt += f"""
The previous plan was rejected for these reasons:
{feedback}

Revise the plan to address the issues.
"""

        response = self.client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2
        )

        raw_output = response.choices[0].message.content.strip()
        # Defensive cleanup for markdown-wrapped JSON
        
        if raw_output.startswith("```"):
            raw_output = raw_output.strip("`")
            raw_output = raw_output.replace("json", "", 1).strip()

        try:
            plan = json.loads(raw_output)
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Planner produced invalid JSON. Raw output:\n{raw_output}"
            ) from e

        return plan
