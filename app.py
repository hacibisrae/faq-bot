"""Application web Flask : affiche la page du chat et répond aux messages."""

from flask import Flask, jsonify, render_template, request

from bot import repondre

app = Flask(__name__)


@app.route("/")
def accueil():
    """Affiche la page web du chatbot."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Reçoit un message en JSON et renvoie la réponse du bot."""
    donnees = request.get_json(silent=True) or {}
    message = donnees.get("message", "")
    return jsonify({"reponse": repondre(message)})


@app.route("/health")
def health():
    """Petit point de contrôle : utile plus tard pour Docker et Kubernetes."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # host="0.0.0.0" rend l'app accessible depuis un conteneur Docker
    app.run(host="0.0.0.0", port=5000, debug=True)
