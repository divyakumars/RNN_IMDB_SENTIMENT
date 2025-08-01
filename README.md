# 🎬 IMDB Movie Review Sentiment Analysis

This is a web app for **Sentiment Analysis** on IMDB-style movie reviews using a Recurrent Neural Network (RNN). The model classifies input reviews as **Positive**, **Negative**, or **Neutral**. Built and launched entirely using **Google Colab** and **Streamlit**.

<img width="782" height="486" alt="image" src="https://github.com/user-attachments/assets/ba9498d8-b1af-4079-82e4-feb2d2c65007" />

---

## 🚀 Features

- 🔍 Analyze the sentiment of any movie review
- 💬 Outputs one of: **Positive**, **Neutral**, or **Negative**
- 🧠 Built using RNN with LSTM layers
- 🌐 Fully interactive web app using Streamlit
- ⚡ Runs live in Colab with a public URL using LocalTunnel

---

## 🧠 Model Overview

- **Architecture**: Embedding Layer → LSTM → Dense Output Layer ->→ Softmax
- **Dataset**: IMDB dataset from Keras (`keras.datasets.imdb`)
- **Classes**: 
  - `Positive 😊`  
  - `Neutral 😐`  
  - `Negative 😞`
- **Preprocessing**:
  - Tokenization and padding
  - Vocabulary size restriction
- **Output**: Class label and prediction confidence score

---

## 🛠️ Installation

### ▶️ How to Run in Colab

### 1. Install Required Packages
```python
!pip install streamlit -q
!pip install pyngrok -q
```
### 2. (Optional) Check your public IP
```
!wget -q -O - ipv4.icanhazip.com
```
### 3. Run Streamlit App with LocalTunnel
```
!streamlit run app.py & npx localtunnel --port 8501
```
🔗 A shareable public URL will be generated — open it to access the app.

---

## 📁 Files in This Repository


### RNN_IMDB_SENTIMENT

```

├── app.py                          # Streamlit application script
├── sentiment_model.keras          # Trained RNN model (TensorFlow native format)
├── Screenshot_2025-08-01_135259.png  # Screenshot of the web app UI
└── README.md                      # This file

```
---

## 🧾 Sample Output
## positive review
<img width="871" height="667" alt="Screenshot 2025-08-01 135226" src="https://github.com/user-attachments/assets/bbac6155-1499-47ef-8f7f-c659e68eb96c" />
<img width="914" height="895" alt="Screenshot 2025-08-01 135240" src="https://github.com/user-attachments/assets/193a9b54-a2dc-4697-a6c2-39abae186d51" />

## neutral review
<img width="987" height="555" alt="Screenshot 2025-08-01 135259" src="https://github.com/user-attachments/assets/964ed872-beef-4f57-a93f-cf1dbe989dae" />


## negative review
<img width="1115" height="734" alt="Screenshot 2025-08-01 135149" src="https://github.com/user-attachments/assets/17283ff9-5655-4ff6-b34b-0427c43a8bf5" />
<img width="1108" height="868" alt="Screenshot 2025-08-01 135206" src="https://github.com/user-attachments/assets/91f5b336-0c75-421f-ae4f-90d203b38589" />

---

## 🧠 Future Improvements

- 🔁 Use Bidirectional LSTM or GRU for better accuracy  
- 💾 Add model caching or reusability features  
- 🌐 Deploy fully on a cloud platform  
- 📊 Add visual charts of sentiment history  
- 📂 Batch review prediction support  

---

## 👨‍💻 Author

**Divya Kumar**  
[GitHub](https://github.com/divyakumars/) • [LinkedIn](www.linkedin.com/in/divyakumar21)

---
