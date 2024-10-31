import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()  # Чтение index.html из общей папки

@app.route('/clear-cache', methods=['POST'])
def clear_cache():
    instructions = (
        "Щоб очистити кеш у браузері:\n"
        "1. Натисніть Ctrl + Shift + Delete (Windows) або Command + Shift + Delete (Mac).\n"
        "2. Оберіть часовий діапазон і тип даних для видалення.\n"
        "3. Натисніть 'Очистити дані'."
    )
    return jsonify({'instructions': instructions})

@app.route('/new-employee', methods=['POST'])
def new_employee():
    instructions = (
        "Ласкаво просимо до компанії! Щоб розпочати, ознайомтеся з інструкціями для нового співробітника.\n"
        "Деталі можна знайти за посиланням внизу сторінки."
    )
    return jsonify({'instructions': instructions})

@app.route('/feature-3', methods=['POST'])
def feature_3():
    instructions = "Інструкції для функції 3."
    return jsonify({'instructions': instructions})

@app.route('/restart-service', methods=['POST'])
def restart_service():
    instructions = (
        "Щоб перезапустити службу:\n"
        "1. Відкрийте 'Диспетчер завдань'.\n"
        "2. Знайдіть потрібну службу.\n"
        "3. Натисніть 'Перезапустити'."
    )
    return jsonify({'instructions': instructions})

@app.route('/check-network', methods=['POST'])
def check_network():
    instructions = (
        "Щоб перевірити мережу:\n"
        "1. Відкрийте 'Командний рядок'.\n"
        "2. Введіть команду 'ping google.com'.\n"
        "3. Переконайтеся, що з'єднання стабільне."
    )
    return jsonify({'instructions': instructions})

@app.route('/manage-process', methods=['POST'])
def manage_process():
    instructions = (
        "Щоб управляти процесами:\n"
        "1. Відкрийте 'Диспетчер завдань'.\n"
        "2. Перейдіть на вкладку 'Процеси'.\n"
        "3. Знайдіть потрібний процес і завершіть або перезапустіть його."
    )
    return jsonify({'instructions': instructions})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
