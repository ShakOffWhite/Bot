import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()  # Чтение index.html из общей папки

@app.route('/clear-cache', methods=['POST'])
def clear_cache():
    instructions = (
        "Чтобы очистить кэш в браузере:\n"
        "1. Нажмите Ctrl + Shift + Delete (Windows) или Command + Shift + Delete (Mac).\n"
        "2. Выберите временной диапазон и тип данных для удаления.\n"
        "3. Нажмите 'Очистить данные'."
    )
    return jsonify({'instructions': instructions})

@app.route('/feature-2', methods=['POST'])
def feature_2():
    instructions = "Здесь будут инструкции для функции 2."
    return jsonify({'instructions': instructions})

@app.route('/feature-3', methods=['POST'])
def feature_3():
    instructions = "Здесь будут инструкции для функции 3."
    return jsonify({'instructions': instructions})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
