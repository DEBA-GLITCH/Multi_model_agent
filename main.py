import json
import sys
from jsonschema import validate, ValidationError

from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from agents.critic_agent import CriticAgent
from memory.audit_log import AuditLog

from config.settings import MAX_ITERATIONS


def load_schema(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def format_plan_for_user(plan: dict) -> str:
    lines = []
    lines.append("Here’s a clear step-by-step plan for you:\n")

    for idx, step in enumerate(plan.get("steps", []), start=1):
        action = step.get("action", "").strip()
        lines.append(f"Step {idx}: {action}")

    return "\n".join(lines)


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
        print("\n🧠 Analyzing your request and preparing a compliant plan...\n")
        audit_log = AuditLog()


        if user_input.lower() in {"exit", "quit"}:
            print("Exiting system.")
            break

        approved = False
        fatal_error = False
        feedback = None

        for iteration in range(1, MAX_ITERATIONS + 1):
            #print(f"\n--- Iteration {iteration} ---")                        >internal debugging only<

            # 1. Planner creates plan

            plan = planner.create_plan(user_input, feedback)

            # Defensive normalization: ensure step.inputs is always an object
            for step in plan.get("steps", []):
                if not isinstance(step.get("inputs"), dict):
                    step["inputs"] = {}


            # 2. Validate plan schema (HARD GATE)

            try:
                validate(instance=plan, schema=plan_schema)
            except ValidationError as e:
                print("❌ Internal planning error. Retrying may help.")
                fatal_error = True
                break  # fatal — no executor run

            # 3. Executor executes plan

            execution_result = executor.execute(plan)

            #print("Execution Result:", execution_result)                       >>internal debugging only<<
            
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

            audit_log.log_iteration(
            user_input=user_input,
            iteration=iteration,
            decision=decision,
            confidence_score=critique.get("confidence_score", 0.0),
            reasons=critique.get("reasons", []),)
           
            print("Critic Decision:", decision)

            if decision == "APPROVE":
                audit_log.log_final_plan(plan)

                print("\n✅ Here’s a clear, compliant plan you can confidently follow:\n")

                formatted_plan = format_plan_for_user(plan)
                print(formatted_plan)

                summary = audit_log.summary()
                confidence = int(summary["confidence_score"] * 100)

                print(f"\n🔒 Confidence level: {confidence}%")
                print("This plan meets standard regulatory and operational requirements.\n")

                break
            else:
                #print("❌ Rejected by Critic, revising plan...")                >>internal debugging only<<
                #print("Reasons:", critique["reasons"])
                #print("Required Changes:", critique["required_changes"])        >>internal debugging only<<

                # ✅ UPDATE feedback here
                feedback = critique["required_changes"]

            if not approved and fatal_error:
                 print("\n⚠️ The request could not be fulfilled due to an internal planning error.")
            elif not approved:
                 print("\n⚠️ Unable to produce a satisfactory plan after multiple attempts.")

if __name__ == "__main__":
    main()    


