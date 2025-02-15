# Blog Generator using LangChain & LLaMA 2  

## Overview  
The **AI Blog Generator** is a **Streamlit-based** web application that generates high-quality blog content using the **LLaMA 2 (7B)** model from Meta.  
It leverages **LangChain** and **CTransformers** to process prompts and generate human-like text responses.  

## Features  
 AI-powered **blog generation** using **LLaMA 2**  
 Customizable **word count** and **target audience**  
**User-friendly UI** built with **Streamlit**  
Seamless **model downloading** from **Hugging Face**  
 **Quick & professional** blog creation  

## 🛠 Tech Stack  
- **Frontend:** Streamlit  
- **Backend:** Python, LangChain, CTransformers  
- **Model:** LLaMA 2 (7B) - GGML format  
- **Deployment:** Local / Cloud-based execution  

---

## 🚀 Installation & Usage  

### 🔹 Clone the Repository  
```bash
git clone https://github.com/your-username/blog-generator-langchain.git
cd blog-generator-langchain
pip install -r requirements.txt
streamlit run app.py
📝 How to Use
Open the AI Blog Generator in your browser.
Enter a Blog Topic.
Select the Word Count and Target Audience.
Click Generate Blog.
The AI will generate a high-quality blog instantly! 🚀
📦 Model Handling
The LLaMA 2 (7B) model is automatically downloaded from Hugging Face when the app runs for the first time.
The model is stored in the models/ directory for efficient reuse.
📌 Requirements
The dependencies required for this application are listed in requirements.txt.
It includes:

Streamlit (For UI)
LangChain (For Prompt Handling)
CTransformers (For Model Execution)
Hugging Face Hub (For Model Download)
🌍 Deployment
🔹 Deploy on Heroku
bash
Copy
Edit
heroku login
heroku create your-app-name
git add .
git commit -m "Initial commit"
git push heroku main
📧 Contact
For queries, feel free to reach out:
📩 Email: dhruvsarin21@gmail.com
