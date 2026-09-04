# An ensemble method is when you combine predictions from several different models instead of relying on just one, 
# because different models tend to make different mistakes — averaging or blending them out usually gives you a more accurate, 
# more stable result than any single model alone.

class EnsembleAgent(Agent):
    name = "Ensemble Agent"
    color = Agent.YELLOW

    def __init__(self):
        self.log("Ensemble Agent is initializing")
        self.specialist = SpecialistAgent()      # your fine-tuned LLM on Modal
        self.frontier = FrontierAgent()           # e.g. GPT-4 + RAG over similar items
        self.random_forest = RandomForestAgent()  # classic ML model on embeddings

    def price(self, description: str) -> float:
        specialist_est = self.specialist.price(description)
        frontier_est = self.frontier.price(description)
        rf_est = self.random_forest.price(description)

        # Simple version: weighted average (weights tuned by hand or via
        # a validation set — e.g. trust the fine-tuned model most)
        final = (0.5 * specialist_est) + (0.3 * frontier_est) + (0.2 * rf_est)

        self.log(f"Ensemble Agent combining ${specialist_est:.2f}, "
                  f"${frontier_est:.2f}, ${rf_est:.2f} -> ${final:.2f}")
        return final

"""
If their errors aren't all correlated in the same direction, averaging them cancels out a lot of that noise — 
the ensemble's error is typically lower than the average error of the individual models.

Averaging / Voting — simplest: just average numeric predictions, or take a majority vote for classification.
Bagging — train the same model type on different random subsets of data, then average (Random Forest = bagged decision trees).
Boosting — train models sequentially, each one fixing the previous one's mistakes (XGBoost, AdaBoost).
Stacking / Blending — train a small "meta-model" whose job is to learn the best way to combine several different base models' 
outputs (not just a flat average — it can learn "trust Model A more when X, Model C more when Y").
"""