import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def answer_question():
    url = request.json['url']
    question = request.json['question']

    # Scrape the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Tokenize the question
    tokens = word_tokenize(question)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Find the answer in the webpage content
    answer = None
    for paragraph in soup.find_all('p'):
        paragraph_tokens = word_tokenize(paragraph.text)
        if all(token in paragraph_tokens for token in tokens):
            answer = paragraph.text
            break

    # Return the answer or "I don't know the answer"
    if answer:
        return jsonify({'answer': answer})
    else:
        return jsonify({'answer': 'I don\'t know the answer'})

if __name__ == '__main__':
    app.run(debug=True)
    
    