from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет, мир!"

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Это данные от сервера"})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json  # Считываем JSON из запроса
    return jsonify({"received": data}), 201  # Возвращаем полученные данные и статус 201 (создано)

if __name__ == '__main__':
    app.run(debug=True)
