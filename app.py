import streamlit as st
import requests

st.title("📊 Decision-Making AI Dashboard")

st.write("Upload product data and get AI recommendation")

# Sample input
data = [
    {
        "product": "Product A",
        "revenue": 50000,
        "growth_rate": 12,
        "cost": 30000,
        "customer_satisfaction": 80
    },
    {
        "product": "Product B",
        "revenue": 60000,
        "growth_rate": 8,
        "cost": 40000,
        "customer_satisfaction": 75
    }
]

if st.button("Run Decision Agent"):
    response = requests.post("http://127.0.0.1:8000/decision", json=data)

    if response.status_code == 200:
        result = response.json()

       # Correct usage
        st.write(result["result"]["decision"])
        st.write(result["latency"])

        st.success(f"✅ Best Product: {result['result']['decision']}")

        st.subheader("📌 Reasoning")
        st.write(result["result"]["reasoning"])

        st.subheader("🤖 LLM Explanation")
        st.write(result["result"].get("llm_explanation", "Not available"))

        st.subheader("⚡ Latency")

        if "latency" in result:
         st.write(result["latency"])
        else:
         st.write("Not available")