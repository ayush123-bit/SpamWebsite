# SpamWebsite

SpamWebsite is a lightweight and interactive web application developed using **Streamlit** for real-time spam detection. This project demonstrates the application of **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques to classify input text messages as either *spam* or *ham* (non-spam).

## 🎯 Objective

The primary goal of this project is to build and deploy a **basic machine learning model** capable of identifying spam messages using classical NLP techniques like **TF-IDF vectorization** and algorithms such as **Multinomial Naive Bayes**.

## 🧠 Model Details

- **Vectorization**: TF-IDF (`tfidf_vectorizer.sav`)
- **Classifier**: Multinomial Naive Bayes (`spammodule.sav`)
- **Framework**: Streamlit for rapid deployment and testing

These models have been pre-trained and serialized using `pickle` or `joblib`, allowing for efficient loading and inference during runtime.

## 📂 Repository Structure

```
SpamWebsite/
├── streamlitspam.py          # Main Streamlit app
├── spammodule.sav            # Saved machine learning model
├── tfidf_vectorizer.sav      # Saved TF-IDF vectorizer
```

## 🚀 Features

- 🧾 Simple and user-friendly interface via Streamlit
- 📈 Real-time prediction of input messages
- ⚡ Fast loading of serialized models for quick classification
- 🧪 Great for demonstrating ML/NLP concepts to beginners

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit**
- **scikit-learn**
- **NLTK**
- **Joblib / Pickle**

## 🧪 How to Run the Project Locally

### Step 1: Clone the Repository
```bash
git clone https://github.com/ayush123-bit/SpamWebsite.git
cd SpamWebsite
```

### Step 2: Create and Activate Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### Step 3: Install Required Libraries
```bash
pip install -r requirements.txt
```

> **Note:** If `requirements.txt` is not available, install manually:
```bash
pip install streamlit scikit-learn nltk joblib
```

### Step 4: Run the Streamlit App
```bash
streamlit run streamlitspam.py
```

Visit `http://localhost:8501` in your browser to access the app.

## 📊 Working Mechanism

1. User enters a message in the input field.
2. Text is vectorized using the pre-trained TF-IDF model.
3. The vector is fed into the Naive Bayes model.
4. The model outputs a prediction: **Spam** or **Not Spam**.

## ✅ Example Output

- Input: `Congratulations! You’ve won a free iPhone. Click the link to claim.`
- Output: `Spam`

- Input: `Hey, are we still on for the meeting tomorrow?`
- Output: `Not Spam`

## 📚 Future Enhancements

- Incorporate advanced deep learning models (e.g., LSTM, BERT)
- Add dataset upload functionality for retraining
- Display model accuracy, confusion matrix, and ROC curve
- Add logging, better exception handling

## 🙋 Author

**Ayush Rai**  
GitHub: [@ayush123-bit](https://github.com/ayush123-bit)

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute with attribution.

---

> **Disclaimer**: This model is trained on a basic dataset and should not be used for production-grade email filtering or security applications.
