# file: app.py

import streamlit as st
import pandas as pd
from datetime import datetime

# ----- Fungsi AI Dummy -----
# Ganti ini dengan LLM / agentic AI yang sebenarnya
def generate_caption(product_name, audience):
    return f"Boost your {product_name} to impress {audience}! 🌟🔥"

def recommend_budget(audience_size):
    # Simple dummy logic
    if audience_size < 1000:
        return 50
    elif audience_size < 5000:
        return 200
    else:
        return 500

# ----- Streamlit UI -----
st.title("Agentic AI Ads Automation Demo")

st.header("Input Campaign Info")
product_name = st.text_input("Product Name", "Skincare Cream")
audience = st.text_input("Target Audience", "Ages 18-25, Female")
audience_size = st.number_input("Audience Size", min_value=100, max_value=100000, value=1000)

if st.button("Generate Campaign"):
    caption = generate_caption(product_name, audience)
    budget = recommend_budget(audience_size)
    
    st.subheader("Generated Campaign")
    st.write(f"**Caption:** {caption}")
    st.write(f"**Recommended Budget ($):** {budget}")

    # ----- Save to CSV -----
    df = pd.DataFrame([{
        "timestamp": datetime.now(),
        "product_name": product_name,
        "audience": audience,
        "audience_size": audience_size,
        "caption": caption,
        "recommended_budget": budget
    }])
    
    # Append to CSV file
    df.to_csv("campaign_history.csv", mode='a', index=False, header=not pd.io.common.file_exists("campaign_history.csv"))
    st.success("Campaign saved to campaign_history.csv!")