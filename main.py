import json
import sys
from jsonschema import validate, ValidationError

from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from agents.critic_agent import CriticAgent

from config.settings import MAX_ITERATIONS


def load_schema(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def main():
    print("Multi-Agent System (Phase 4)")
    print("Type 'exit' or 'quit' to stop.\n")



    # Load schemas



    try:
        plan_schema = load_schema("schemas/plan_schema.json")
        critique_schema = load_schema("schemas/critique_schema.json")
    except Exception as e:
        print("❌ Failed to load schemas:", e)
        sys.exit(1)

    planner = PlannerAgent()
    executor = ExecutorAgent()
    critic = CriticAgent()

    while True:
        user_input = input("User > ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Exiting system.")
            break

        approved = False
        feedback = None

        for iteration in range(1, MAX_ITERATIONS + 1):
            print(f"\n--- Iteration {iteration} ---")


            # 1. Planner creates plan


            plan = planner.create_plan(user_input, feedback)



            # 2. Validate plan schema (HARD GATE)



            try:
                validate(instance=plan, schema=plan_schema)
            except ValidationError as e:
                print("❌ Plan schema validation failed.")
                print("Error:", e.message)
                break  # fatal — no executor run

            # 3. Executor executes plan

            execution_result = executor.execute(plan)
            print("Execution Result:", execution_result)
            
            # 4. Critic reviews

            critique = critic.review(plan, execution_result)

            # 5. Validate critique schema


            try:
                validate(instance=critique, schema=critique_schema)
            except ValidationError as e:
                print("❌ Critique schema validation failed.")
                print("Error:", e.message)
                break  # fatal — system error


            # 6. Decision enforcement

            decision = critique["decision"]
            print("Critic Decision:", decision)

            if decision == "APPROVE":
                print("\n✅ Final Approved Output:")
                print(execution_result)
                approved = True
                break
            else:
                print("❌ Rejected by Critic.")
                print("Reasons:", critique["reasons"])
                print("Required Changes:", critique["required_changes"])

                # ✅ UPDATE feedback here
                feedback = critique["required_changes"]


        if not approved:
            print("\n⚠️ Max iterations reached or fatal error occurred.")
            print("No approved output produced.")
        


        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
