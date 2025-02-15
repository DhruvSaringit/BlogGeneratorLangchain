import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import os
from huggingface_hub import hf_hub_download


# Function to download the LLaMA model
def download_model():
    model_path = "models/llama-2-7b-chat.ggmlv3.q8_0.bin"
    if not os.path.exists(model_path):
        model_path = hf_hub_download(repo_id="TheBloke/Llama-2-7B-Chat-GGML",
                                     filename="llama-2-7b-chat.ggmlv3.q8_0.bin",
                                     local_dir="models")
    return model_path


# Function to get LLaMA response
def getLLamaresponse(input_text, no_words, blog_style):
    model_path = download_model()

    llm = CTransformers(model=model_path,
                        model_type='llama',
                        config={'max_new_tokens': 256, 'temperature': 0.01})

    # Blog prompt template
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)

    # Generate response
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response


# --------------- Streamlit UI Design ----------------
st.set_page_config(page_title="AI Blog Generator", page_icon="📝", layout="centered")

# Custom CSS for a clean UI
st.markdown("""
    <style>
        .main {background-color: #f4f4f4;}
        .stTextInput, .stSelectbox, .stNumberInput {width: 100%;}
        .stButton>button {width: 100%; background-color: #4CAF50; color: white; padding: 10px 20px; font-size: 18px; border-radius: 8px;}
        .stButton>button:hover {background-color: #45a049;}
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<h1 style='text-align: center; color: #333;'>🚀 AI Blog Generator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666;'>Generate high-quality blogs instantly with LLaMA 2</h3>",
            unsafe_allow_html=True)
st.write("---")

# Sidebar
with st.sidebar:

    st.markdown("## 🔥 About This App")
    st.write("This AI-powered app generates professional blogs using **LLaMA 2** from Meta.")
    st.markdown("#### ✨ Features")
    st.write("- Generates **high-quality** blog content.")
    st.write("- **Custom word count** & writing style.")
    st.write("- **Powered by LLaMA 2 (7B)** model.")
    st.write("---")
    st.write("🔗 [Hugging Face Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)")

# Input Fields
st.markdown("### ✍️ Enter Blog Details")
input_text = st.text_input("📌 Blog Topic", placeholder="e.g. Future of AI in Healthcare")

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.number_input('📏 Word Count', min_value=50, max_value=1000, value=300, step=50)
with col2:
    blog_style = st.selectbox("✒️ Target Audience", ("Researchers", "Data Scientist", "Common People"), index=0)

# Generate Button
submit = st.button("🚀 Generate Blog")

if submit:
    if not input_text:
        st.error("⚠️ Please enter a blog topic.")
    else:
        with st.spinner("⏳ Generating your blog..."):
            blog_content = getLLamaresponse(input_text, no_words, blog_style)
        st.success("✅ Blog Generated Successfully!")

        # Display the blog
        st.markdown("### 📝 Your AI-Generated Blog")
        st.write(blog_content)
