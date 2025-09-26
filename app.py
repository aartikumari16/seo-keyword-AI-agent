import streamlit as st
import requests

st.set_page_config(page_title="SEO Keyword Research Agent", layout="wide")

st.title("🔍 SEO Keyword Research Agent")

st.write("Enter a seed keyword below and get keyword suggestions (from n8n workflow).")

# Input box for seed keyword
seed_keyword = st.text_input("Seed Keyword:", "")

if st.button("Generate Keywords"):
    if not seed_keyword.strip():
        st.warning("Please enter a seed keyword.")
    else:
        try:
            # Call your n8n webhook (make sure n8n is running)
            url = "http://localhost:5678/webhook/seo-keywords"   # Production
            # url = "http://localhost:5678/webhook-test/seo-keywords"  # For testing in n8n editor
            
            response = requests.post(url, json={"seed_keyword": seed_keyword})
            
            if response.status_code == 200:
                keywords = response.json()
                
                if isinstance(keywords, list) and len(keywords) > 0:
                    st.success(f"✅ Found {len(keywords)} keywords for '{seed_keyword}'")
                    st.dataframe(keywords)
                else:
                    st.warning("No keywords returned from workflow.")
            else:
                st.error(f"Error from API: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Failed to connect: {e}")
