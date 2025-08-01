import streamlit as st
from keras.models import load_model
from keras.preprocessing import sequence
from keras.datasets import imdb
import matplotlib.pyplot as plt

# Load the IMDB dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load the trained model
@st.cache_resource
def load_sentiment_model():
    return load_model('simple_rnn_imdb.h5')


model = load_sentiment_model()

# Preprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# Predict sentiment with 3 classes
def predict_sentiment(review, neutral_margin=0.05):
    preprocessed_input = preprocess_text(review)
    prediction = model.predict(preprocessed_input, verbose=0)
    score = float(prediction[0][0])
    
    if score >= 0.55:
        sentiment = 'Positive'
    elif score <= 0.45:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, score

# Streamlit UI
st.set_page_config(page_title="IMDB Sentiment Analysis", layout="centered")
st.title("🎬 IMDB Movie Review Sentiment Analysis")
st.markdown("Enter a movie review below to predict the sentiment:")

user_input = st.text_area("📝 Movie Review", height=150, placeholder="e.g. This movie was absolutely amazing!")

# Sample Suggestions
with st.expander("💡 Try Sample Reviews"):
    st.markdown("- 😊 Absolutely loved it! Would definitely recommend.")
    st.markdown("- 😐 It was just okay, not too bad, not too great.")
    st.markdown("- 😡 Terrible acting and weak storyline.")

# Predict Sentiment
if st.button("🔍 Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        sentiment, score = predict_sentiment(user_input)
        
        # Show result
        if sentiment == 'Positive':
            st.success(f"😊 Sentiment: **Positive** (Score: {score:.4f})")
        elif sentiment == 'Negative':
            st.error(f"😡 Sentiment: **Negative** (Score: {score:.4f})")
        else:
            st.info(f"😐 Sentiment: **Neutral** (Score: {score:.4f})")

        # Show sentiment score bar chart
        st.markdown("### 📊 Sentiment Probability")
        labels = ['Negative', 'Neutral', 'Positive']
        values = [1 - score if score < 0.45 else 0,
                  score if 0.45 <= score <= 0.55 else 0,
                  score if score > 0.55 else 0]

        fig, ax = plt.subplots()
        ax.bar(labels, values, color=["red", "orange", "green"])
        ax.set_ylim([0, 1])
        st.pyplot(fig)
