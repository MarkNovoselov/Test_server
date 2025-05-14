from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'downloads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/') # проверка связи
def home():
    return "Сервер работает!"

@app.route('/json', methods=['POST']) # отправка json
def json_endpoint():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Нет JSON'}), 400
    return jsonify({'status': 'успешно', 'received': data})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
