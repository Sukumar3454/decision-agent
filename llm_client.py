import requests

def generate_explanation(data, decision):
    prompt = f"""
    You are a business analyst.

    Given the following product data:
    {data}

    Explain why '{decision}' is the best product to invest in.
    Keep explanation short and clear.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]