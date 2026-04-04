from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Configura tu API Key desde las variables de entorno en Render
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensaje = data.get("mensaje")

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",   # puedes usar gpt-4 si tu cuenta lo permite
            messages=[{"role": "user", "content": mensaje}]
        )

        texto = respuesta.choices[0].message["content"]
        return jsonify({"respuesta": texto})

    except Exception as e:
        return jsonify({"respuesta": f"Error: {str(e)}"})
