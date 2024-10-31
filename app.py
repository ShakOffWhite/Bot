import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/clear-cache', methods=['POST'])
def clear_cache():
    instructions = (
        "Щоб очистити кеш у браузері:\n"
        "1. Натисніть Ctrl + Shift + Delete (Windows) або Command + Shift + Delete (Mac).\n"
        "2. Виберіть часовий діапазон та тип даних для видалення.\n"
        "3. Натисніть 'Очистити дані'."
    )
    return jsonify({'instructions': instructions})

@app.route('/restart-service', methods=['POST'])
def restart_service():
    instructions = (
        "Щоб перезапустити службу:\n"
        "1. Відкрийте командний рядок від імені адміністратора.\n"
        "2. Введіть 'net stop <назва служби>' та натисніть Enter.\n"
        "3. Введіть 'net start <назва служби>' та натисніть Enter."
    )
    return jsonify({'instructions': instructions})

@app.route('/check-network', methods=['POST'])
def check_network():
    instructions = (
        "Щоб перевірити стан мережі:\n"
        "1. Відкрийте командний рядок.\n"
        "2. Введіть 'ping google.com' та натисніть Enter.\n"
        "3. Переконайтесь, що ви отримуєте відповідь від сервера."
    )
    return jsonify({'instructions': instructions})

@app.route('/manage-process', methods=['POST'])
def manage_process():
    instructions = (
        "Щоб завершити процес:\n"
        "1. Відкрийте диспетчер завдань.\n"
        "2. Знайдіть потрібний процес у списку.\n"
        "3. Натисніть правою кнопкою миші та виберіть 'Завершити завдання'."
    )
    return jsonify({'instructions': instructions})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
