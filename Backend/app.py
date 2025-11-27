from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita acceso desde el frontend

@app.route('/')
def home():
    return jsonify({"message": "API Backend Operativa", "status": "OK"})

@app.route('/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    if not data or 'num1' not in data or 'num2' not in data:
        return jsonify({"error": "Faltan datos"}), 400
    
    try:
        resultado = float(data['num1']) + float(data['num2'])
        return jsonify({"resultado": resultado})
    except ValueError:
        return jsonify({"error": "Los valores deben ser numéricos"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)