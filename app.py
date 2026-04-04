from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Usa la API Key desde la variable de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "")

    # Llamada a OpenAI
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mensaje}]
    )

    texto = respuesta.choices[0].message.content
    return jsonify({"respuesta": texto})

if __name__ == "__main__":
    app.run(debug=True)
