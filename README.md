# CodeAlpha_SentimentAnalysis

# ✅ Task 4: Sentiment Analysis

## 📌 Objective

Analyze a set of text samples (user opinions) to classify them as **Positive** or **Negative** using a simple, beginner-friendly Python program — **without** using any external NLP libraries like `TextBlob` or `sklearn`.

---

## 📂 Dataset

**File:** `sentiment_dataset.csv`

| Text                          | Sentiment |
|-------------------------------|-----------|
| I love this product           | Positive  |
| This is awful                 | Negative  |
| Very happy with the service   | Positive  |
| I am sad and disappointed     | Negative  |
| Best experience ever          | Positive  |
| Worst thing ever              | Negative  |

---

## 🧠 Approach

- A basic **keyword-matching** strategy is used for sentiment classification.
- Manually defined positive and negative word lists.
- For each text entry, if it contains a positive word → marked "Positive", negative word → "Negative".

---

## 🛠️ Tools & Libraries Used

- Python 🐍
- pandas

No external NLP or ML libraries required — ideal for absolute beginners!

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-task.git
   cd sentiment-analysis-task
