
# 🧠 Prompt Engineering Playground

An interactive web application to experiment with Large Language Models (LLMs) by tuning parameters like **temperature**, **top_p**, and **max tokens** in real time.

This project helps understand how prompt design and parameter tuning influence AI-generated responses.

---

## 🚀 Demo

*(Add your deployed link here – Streamlit Cloud / AWS / Render)*

---

## 📌 Features

* ✍️ Enter custom prompts
* 🎛️ Adjust LLM parameters:

  * Temperature (creativity)
  * Top_p (probability sampling)
  * Max Tokens (response length)
* ⚡ Real-time response generation
* 🔄 Interactive UI with instant feedback
* 🧪 Helps analyze hallucination & response variation

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **OpenAI API** (LLM)
* **python-dotenv** (environment variables)

---

## 🧱 Project Structure

```
prompt-playground/
│
├── app.py              # Streamlit UI
├── llm.py              # LLM API logic
├── .env                # API key (not pushed)
├── requirements.txt    # Dependencies
├── README.md           # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/prompt-playground.git
cd prompt-playground
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters a prompt in the UI
2. Selects parameters (temperature, top_p, max_tokens)
3. App sends request to LLM via API
4. LLM generates response
5. Output is displayed in real time

---

## 🎯 Learning Outcomes

* Understanding **prompt engineering techniques**
* Controlling LLM behavior using parameters
* Handling **hallucinations and response variability**
* Building interactive AI applications using Streamlit
* Integrating external APIs securely using `.env`

---

## 📊 Example Use Cases

* Text summarization
* Email drafting
* Concept explanation
* Creative writing
* Prompt experimentation

---

## ⚡ Future Improvements

* 🔁 Compare multiple outputs side-by-side
* 🧠 Add system prompt customization
* 💾 Save prompt history
* 📊 Token usage tracking
* 🌐 Deploy with authentication

---

## 📸 Screenshots

*(Add screenshots of your app here)*
<img width="956" height="481" alt="image" src="https://github.com/user-attachments/assets/f071ff66-8df3-4a5f-9889-5ecbf1f58abf" />

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Author

**Suraj Satav**
AI / Generative AI Enthusiast 🚀
