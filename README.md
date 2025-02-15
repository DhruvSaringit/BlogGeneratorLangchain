# BlogGeneratorLangchain
Overview

The AI Blog Generator is a Streamlit-based web application that generates high-quality blog content using LLaMA 2 (7B) model from Meta. The application utilizes LangChain and CTransformers to process prompts and generate human-like text responses.

Features
AI-powered blog generation using LLaMA 2
Customizable word count and target audience
User-friendly UI built with Streamlit
Seamless model downloading from Hugging Face
Quick & professional blog creation

🛠Tech Stack
Frontend: Streamlit
Backend: Python, LangChain, CTransformers
Model: LLaMA 2 (7B) - GGML format
Deployment: Local/Cloud-based execution

The model LLaMA 2 (7B) is automatically downloaded from Hugging Face when first running the app. It is stored in the models/ directory.

Open the AI Blog Generator in your browser.
Enter a Blog Topic.
Select the Word Count and Target Audience.
Click Generate Blog.
The AI will generate a high-quality blog instantly!

Requirements
The dependencies required for this application are listed in requirements.ixi. It includes:
Streamlit (For UI)
LangChain (For Prompt Handling)
CTransformers (For Model Execution)
Hugging Face Hub (For Model Download)
