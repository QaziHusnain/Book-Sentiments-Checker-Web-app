import nltk
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer

st.title("Check Sentimentals of Book")
uploaded_file = st.file_uploader("Upload a text file",type=["txt"])

if uploaded_file is not None:
    # Process the uploaded file
    # For example, you can read and display the contents of the file
    file_contents = uploaded_file.read().decode("utf-8")
    analyzer=SentimentIntensityAnalyzer()
    score=analyzer.polarity_scores(file_contents)
    st.write(f"Negativity:{score['neg']}")
    st.write(f"Positivity:{score['pos']}")
    st.write(f"Neutrality:{score['neu']}")


    if score["compound"]>=0:
        st.subheader("This is look a Positive sentimental Book")
    else:
        st.subheader("This is look a Negative sentimental Book")





else:
    st.write("upload a book in text format and gets its sentimentals result")


