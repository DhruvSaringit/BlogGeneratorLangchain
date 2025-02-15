# Blog Generator using LangChain & LLaMA 2  

## Overview  
The **AI Blog Generator** is a **Streamlit-based** web application that generates high-quality blog content using the **LLaMA 2 (7B)** model from Meta.  
It leverages **LangChain** and **CTransformers** to process prompts and generate human-like text responses.  

## Features  
✅ AI-powered **blog generation** using **LLaMA 2**  
✅ Customizable **word count** and **target audience**  
✅ **User-friendly UI** built with **Streamlit**  
✅ Seamless **model downloading** from **Hugging Face**  
✅ **Quick & professional** blog creation  

---

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

## Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

 Run the Application
bash
Copy
Edit
streamlit run app.py

###**Model Handling**
The LLaMA 2 (7B) model is automatically downloaded from Hugging Face when the app runs for the first time.
The model is stored in the models/ directory for efficient reuse.
