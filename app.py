import os
import subprocess
import logging
from flask import Flask, jsonify, send_from_directory, request

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/run', methods=['POST'])
def run_exe():
    try:
        exe_path = os.path.join(os.path.dirname(__file__), 'menuu.exe')
        
        # Проверьте, что файл существует
        if os.path.exists(exe_path):
            logging.info(f'Файл найден: {exe_path}')
            
            # Запуск загруженного файла с использованием wine
            result = subprocess.run(['wine', exe_path], capture_output=True, text=True)
            return jsonify({'output': result.stdout, 'error': result.stderr}), 200
        else:
            logging.error(f'Файл не найден: {exe_path}')
            return jsonify({'error': 'Файл не найден'}), 404
    except Exception as e:
        logging.error(f'Ошибка: {str(e)}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
