from flask import Flask, request, jsonify, send_from_directory
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/run', methods=['POST'])
def run_exe():
    try:
        # Укажите путь к вашему .exe файлу
        result = subprocess.run(['C:/Users/v.morozov/Desktop/My test/teams-app/menuu.exe'], capture_output=True, text=True)
        return jsonify({'output': result.stdout, 'error': result.stderr}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
