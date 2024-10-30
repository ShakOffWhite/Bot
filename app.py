from flask import Flask, request, jsonify, send_from_directory
import webbrowser
import subprocess
import tempfile
import os
import shutil

app = Flask(__name__)

# Функции для кнопок
def open_link(url):
    webbrowser.open(url)

def clear_temp_cache():
    temp_dir = tempfile.gettempdir()
    try:
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)
            try:
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
            except Exception as e:
                print(f"Не удалось удалить {item_path}: {e}")
        print("Временные файлы очищены.")
    except Exception as e:
        print(f"Ошибка при очистке временных файлов: {e}")

def reset_network_settings():
    commands = [
        "ipconfig /release", "ipconfig /renew", "arp -d *",
        "nbtstat -R", "nbtstat -RR", "ipconfig /flushdns",
        "ipconfig /registerdns"
    ]
    for command in commands:
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Ошибка выполнения команды {command}: {e}")
    print("Сетевые настройки сброшены.")

def map_network_drives():
    commands = [
        'net use S: "\\\\192.168.51.254\\Work" /PERSISTENT:YES',
        'net use W: "\\\\192.168.51.254\\Shares" /PERSISTENT:YES',
        'net use Z: "\\\\192.168.51.254\\Archive$" /PERSISTENT:YES',
        'net use X: "\\\\192.168.51.254\\Exchange" /PERSISTENT:YES'
    ]
    for command in commands:
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Ошибка выполнения команды {command}: {e}")
    print("Сетевые диски подключены.")

# Эндпоинты для кнопок
@app.route('/open_link/<int:link_id>', methods=['GET'])
def handle_link(link_id):
    links = {
        1: "https://bim-ae-force.monday.com/boards/5998729170/views/130797164",
        2: "https://bimleaders-my.sharepoint.com/:x:/r/personal/hryhoriv_bim-ae_com/_layouts/15/Doc.aspx?sourcedoc=%7B9C51368B-2D21-4166-8483-DF7325426AA0%7D&file=AnyDesk%20passwords.xlsx&fromShare=true&action=default&mobileredirect=true&wdOrigin=TEAMS-MAGLEV.p2p_ns.rwc&wdExp=TEAMS-TREATMENT&wdhostclicktime=1730119856857&web=1",
        3: "https://bimleaders-my.sharepoint.com/:x:/g/personal/nazarchuk_bim-ae_com/EaeK85LyE2tNhy5IQrdJy6YBmJGDDXjFZmV46C-tqUNZ9w?wdOrigin=TEAMS-MAGLEV.p2p_ns.rwc&wdExp=TEAMS-TREATMENT&wdhostclicktime=1730120958850&web=1",
        4: "https://outlook.office.com/mail/",
        5: "https://make.powerautomate.com/environments/Default-a131aa43-5b0a-451f-a250-e8b038367aa2/flows"
    }
    
    url = links.get(link_id)
    if url:
        open_link(url)
        return jsonify({"message": "Link opened."}), 200
    else:
        return jsonify({"error": "Link not found."}), 404

@app.route('/clear_temp_cache', methods=['POST'])
def clear_temp_cache_endpoint():
    clear_temp_cache()
    return jsonify({"message": "Temporary files cleared."}), 200

@app.route('/reset_network', methods=['POST'])
def reset_network():
    reset_network_settings()
    return jsonify({"message": "Network settings reset."}), 200

@app.route('/map_network_drives', methods=['POST'])
def map_drives():
    map_network_drives()
    return jsonify({"message": "Network drives mapped."}), 200

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
