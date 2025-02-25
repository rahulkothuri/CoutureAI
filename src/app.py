import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from serpapi import GoogleSearch
import os

@st.cache_resource
def load_model():
    pipeline = StableDiffusionPipeline.from_pretrained(
        "amulya15/stablediffusionfinetuned/", torch_dtype=torch.float16
    )
    pipeline.to("cuda")
    return pipeline

pipeline = load_model()

# Streamlit app
st.title("CoutureAI: Clothing Image Generator")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            image = pipeline(prompt).images[0]
            st.image(image, caption="Generated Image", use_container_width=True)
    else:
        st.warning("Please enter a prompt.")

    # Get product recommendations from Google Shopping
    params = {
        "engine": "google_shopping",
        "q": prompt,  # Use the prompt for the search query
        "api_key": "YOUR_API_KEY"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    # Display recommendations
    st.header("Recommended Products")
    for product in results.get("shopping_results", []):
        st.write(product.get("title"))
        st.image(product.get("thumbnail"))
        st.write(product.get("link"))

# Set environment variable for localtunnel
os.environ["LOCALTUNNEL_ bypass-tunnel-reminder "] = "true"