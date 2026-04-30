import streamlit as st
from llm import generate_response

st.set_page_config(page_title="Prompt Playground", layout="wide")

st.title("🧠 Prompt Engineering Playground")

# Sidebar controls
st.sidebar.header("⚙️ Parameters")

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 1.0)
max_tokens = st.sidebar.slider("Max Tokens", 50, 1000, 300)

# Prompt input
prompt = st.text_area("✍️ Enter your prompt:", height=200)

if st.button("🚀 Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            output = generate_response(prompt, temperature, top_p, max_tokens)
        
        st.subheader("💡 Output")
        st.write(output)
    else:
        st.warning("Please enter a prompt!")