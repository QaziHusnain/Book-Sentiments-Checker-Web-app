import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
from pathlib import Path
import plotly.express as px
filepaths=glob.glob("diary/*.txt")
post_lis=[]
neg_lis=[]
date_lis=[]

for filepath in filepaths:

    with open(filepath,"r") as file:
        text=file.read()
    date=Path(filepath).stem
    date_lis.append(date)
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    post_lis.append(score["pos"])
    neg_lis.append(score["neg"])

st.title("Positivity Garph in Diary")

figure = px.line(x=date_lis, y=post_lis, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(figure)
st.title("Negativity Garph in Diary")
figure = px.line(x=date_lis, y=neg_lis, labels={"x": "Dates", "y": "Negativity "})
st.plotly_chart(figure)