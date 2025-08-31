# QuantumRead: High-Speed URL Summarizer
QuantumRead is a powerful yet simple web application that generates detailed summaries from any YouTube video or website URL. Built with Streamlit and powered by the high-speed Groq inference engine, this tool allows you to quickly understand the content of a link without having to read through the entire text or watch the whole video.

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit)
![LLM](https://img.shields.io/badge/LLM-Groq%20%7C%20LangChain%20%7C%20Gemma_2-blueviolet)
![Language](https://img.shields.io/badge/Language-Python_3.11-yellow?logo=python)  

## 📝 Table of Contents
- [📌 About the Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [🛠️ Requirements](#️-requirements)
- [🚀 How to Run](#-how-to-run)
- [🖼️ Sample Interface](#-sample-interface)
- [📄 License](#-license)
- [📧 Contact](#-contact)
---
## 📌 About the Project

This project leverages the power of Large Language Models (LLMs) to provide on-demand summaries. By simply providing a URL, users can get a concise overview of the content, making it an ideal tool for research, learning, and quick information gathering. It uses LangChain to structure the interaction with the Groq API and intelligently load data from different web sources.

---

## ✨ Key Features
  * **Dual Source Summarization:** Supports both YouTube videos and general website URLs.
  * **High-Speed Inference:** Utilizes Groq's low-latency engine for near-instantaneous summary generation.
  * **User-Friendly Interface:** A clean and simple UI built with Streamlit for ease of use.
  * **Robust Error Handling:** Provides clear feedback for invalid URLs and incorrect API keys.
  * **Secure API Key Input:** Uses a password field to keep your Groq API key confidential.

---
## 🛠️ Requirements

You can install all the necessary Python packages by creating a `requirements.txt` file with the content below and running the following command:

```bash 
pip install -r requirements.txt
```
---

## 🚀 How to Run

**1. Clone the Repository**
```
git clone https://github.com/syed-masood-pro/QuantumRead.git
cd QuantumRead
```

**2. Install Dependencies**
```
pip install -r requirements.txt
```

**3. Get Your API Keyt**

You will need a free API key from [Groq](https://console.groq.com/keys).

**4. Run the Streamlit App**

From your terminal, run the following command to start the application (assuming your file is named `app.py`):
```bash
streamlit run app.py
```
The app will open in your web browser. Enter your Groq API key in the sidebar, paste a URL, and click `Summarize` to get started.

---

## 🖼️ Sample Interface

**Initial View**
<img width="959" height="473" alt="proj1" src="https://github.com/user-attachments/assets/73e93105-3f68-4835-9c9b-921e88344744" />

**YouTube Summary Example**
<img width="950" height="474" alt="proj2" src="https://github.com/user-attachments/assets/82c949ab-f7f1-4c03-ac00-663e20e811d2" />

**Website Summary Example**
<img width="949" height="475" alt="proj3" src="https://github.com/user-attachments/assets/bac56124-2c4c-4c32-8dff-d76ec47dc332" />

---

## 📄 License

This project is licensed under the MIT License.

---

## 📧 Contact
**Syed Masood**

✉️ [syedmasood.pro@gmail.com](syedmasood.pro@gmail.com)

🔗 [GitHub Profile](https://github.com/syed-masood-pro/)

💼 [LinkedIn](https://www.linkedin.com/in/syed-masood-pro/)
