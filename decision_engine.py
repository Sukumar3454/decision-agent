def calculate_score(product):
    score = (
        product["revenue"] * 0.3 +
        product["growth_rate"] * 0.3 +
        product["customer_satisfaction"] * 0.2 -
        product["cost"] * 0.2
    )
    return score


def make_decision(products):
    scores = []
    reasoning = []
    steps = []

    steps.append("Starting evaluation of products")
    
    for product in products:
        score = calculate_score(product)
        scores.append({
            "product": product["product"],
            "score": score
        })
        reasoning.append(
            f"{product['product']} → Score calculated using revenue, growth, satisfaction, and cost"
        )

    steps.append("Calculated scores for all products")

    # Find best product
    best = max(scores, key=lambda x: x["score"])
    steps.append("Selected product with highest score")

    reasoning.append(f"{best['product']} has the highest overall score")

    return {
        "decision": best["product"],
        "score_summary": scores,
        "reasoning": reasoning,
        "steps": steps
    }