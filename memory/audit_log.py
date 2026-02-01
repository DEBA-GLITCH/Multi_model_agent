from datetime import datetime

class AuditLog:
    def __init__(self):
        self.records = []

    def log_iteration(
        self,
        user_input: str,
        iteration: int,
        decision: str,
        confidence_score: float,
        reasons: list,
    ):
        self.records.append({
            "timestamp": datetime.utcnow().isoformat(),
            "user_input": user_input,
            "iteration": iteration,
            "decision": decision,
            "confidence_score": confidence_score,
            "reasons": reasons,
        })

    def log_final_plan(self, plan: dict):
        self.final_plan = plan

    def summary(self):
        return {
            "total_iterations": len(self.records),
            "final_decision": self.records[-1]["decision"]
            if self.records else None,
            "confidence_score": self.records[-1]["confidence_score"]
            if self.records else None,
        }
