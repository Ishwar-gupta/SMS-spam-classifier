import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


import string
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text) #Breaks the sentence into individual words and punctuation.

    y=[] #Creates an empty list.
    for i in text:
        if i.isalnum():#It checks whether the string contains only alphabets and numbers i.e no punctuation
            y.append(i) #Adds valid words into the list.

    text = y[:] #This copies the contents of y into text.
    y.clear()

    for i in text:
        if i not in stopwords.words("english") and i not  in string.punctuation: # this removes stopwords and punctuation
            y.append(i) #Adds only useful words.

    text = y[:]
    y.clear()

    # stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)
    

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

# this is the title of the project
st.title("Email/SMS Spam Classifier")

# input_feild for the message
input_sms = st.text_input("Enter the message:")

# button for predict the spam or not
if st.button("Predict"):
# 1. preprocess 
    transformed_sms = transform_text(input_sms)

    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])

    # 3. predict
    result = model.predict(vector_input)[0]

    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
