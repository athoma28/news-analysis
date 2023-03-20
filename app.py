# app.py
from flask import Flask, render_template, request, jsonify
import openai
import json

openai.api_key = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    # Extract the article text from the incoming request data
    request_data = request.get_json()
    article_text = request_data['text']

    # Pass the article text into the messages body

    x = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages=[
            {
                "role": "system",
                "content": "You are a highly advanced AI assistant that can analyze news articles and provide summaries, key people and places, and key data points. You return perfect JSON-formatted summaries every time."
            },
            {
                "role": "user",
                "content": f"Please analyze the following news article: '{article_text}'. Provide a brief summary, key people and places, and key data points in JSON format. The response should be structured in JSON format with no additional comments. The response should be structured like this: {{'summary': '...', 'people_and_places': ['...', '...'], 'data_points': ['...', '...']}}. However, make sure you replace all single quotes with double quotes in your example."
            }
        ]
    )
    json_data = json.loads(x["choices"][0]["message"]["content"])
    return jsonify(json_data)

@app.route('/api/question', methods=['POST'])
def question():
    # Extract the article text from the incoming request data
    request_data = request.get_json()
    article_text = request_data['text']
    user_question = request_data['question']

    # Pass the article text into the messages body

    x = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages=[
            {
                "role": "system",
                "content": "You are a highly advanced AI assistant that can analyze news articles and answer questions about them."
            },
            {
                "role": "user",
                "content": f"Please analyze the following news article: '{article_text}'.'{user_question}'?"
            }
        ]
    )
    return x["choices"][0]["message"]["content"]


if __name__ == '__main__':
    app.run(debug=True)

#
# def debug_analyze(article_text):
#
#     # Pass the article text into the messages body
#
#     x = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         temperature=1,
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a highly advanced AI assistant that can analyze news articles and provide summaries, key people and places, and key data points."
#             },
#             {
#                 "role": "user",
#                 "content": f"Please analyze the following news article: '{article_text}'. Provide a brief summary, key people and places, and key data points in JSON format. The response should be structured in JSON format with no additional comments. The JSON property names should be (in double quotes) summary, people_and_places, and data_points."
#             }
#         ]
#     )
#     json_data = json.loads(x["choices"][0]["message"]["content"])
#     return jsonify(json_data)
#
#
# print(debug_analyze("Coffee in Vietnam is social, said Mindfully Cafe's Ngan. Friends like to dine at a restaurant, then move to a coffeehouse for a drink -- relocating is part of the routine. Or they like to watch the street from a cafe, at times on the street itself -- a feature that sets sidewalk vendors apart from Starbucks."))
#
