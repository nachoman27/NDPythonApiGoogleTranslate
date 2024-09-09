from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def translate_text():
    translator = Translator()
    translations = {}
    
    if request.method == "POST":
        text = request.form["text"]
        
        # Lista de idiomas de destino
        languages = ['en', 'fr', 'de', 'it', 'pt']  # Inglés, Francés, Alemán, Italiano, Portugués
        
        for lang in languages:
            translated = translator.translate(text, dest=lang)
            translations[lang] = translated.text

    return render_template("index.html", translations=translations)

if __name__ == "__main__":
    app.run(debug=True)
