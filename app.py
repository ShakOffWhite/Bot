import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Получаем ключ API из переменной окружения
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    answer = response['choices'][0]['message']['content']
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
