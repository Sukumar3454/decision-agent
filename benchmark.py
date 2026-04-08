from decision_engine import make_decision

test_cases = [
    {
        "input": [
            {"product": "A", "revenue": 50000, "growth_rate": 10, "cost": 20000, "customer_satisfaction": 80},
            {"product": "B", "revenue": 40000, "growth_rate": 8, "cost": 25000, "customer_satisfaction": 70}
        ],
        "expected": "A"
    }
]

correct = 0

for test in test_cases:
    result = make_decision(test["input"])
    if result["decision"] == test["expected"]:
        correct += 1

accuracy = correct / len(test_cases)
print("Accuracy:", accuracy)