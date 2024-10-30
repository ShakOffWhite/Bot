from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Установите ваш OpenAI API ключ
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

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
