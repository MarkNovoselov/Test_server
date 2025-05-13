from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/') # проверка связи
def home():
    return "Сервер работает!"

@app.route('/json', methods=['POST']) # отправка json
def json_endpoint():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Нет JSON'}), 400
    print(f"Получен JSON: {data}")
    return jsonify({'status': 'успешно', 'received': data})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename): # скачивание файла клиентом
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'Файл не найден'}), 404
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
