from flask import Flask, jsonify, send_from_directory
import subprocess
import os
import requests

app = Flask(__name__)

# URL для загрузки файла (замените на ваш)
GITHUB_URL = 'https://raw.githubusercontent.com/ShakOffWhite/Bot/9916a55f9ac89b707559b7d980ec59267607bb86/menuu.exe'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/run', methods=['POST'])
def run_exe():
    try:
        # Загрузка файла с GitHub
        response = requests.get(GITHUB_URL)
        exe_path = os.path.join(os.path.dirname(__file__), 'menuu.exe')
        
        # Запись файла на диск
        with open(exe_path, 'wb') as f:
            f.write(response.content)

        # Запуск загруженного файла
        result = subprocess.run([exe_path], capture_output=True, text=True)
        return jsonify({'output': result.stdout, 'error': result.stderr}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
