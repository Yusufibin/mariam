import os

import openai
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
temperature=0.9,
  max_tokens=3000,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
        )
        return redirect(url_for("index", result=response.choices[0].text))
    # Sauvegarder le contenu de la variable "result" dans un fichier texte
    
    result = request.args.get("result")
    with open("static/result.txt", "w") as f:
        f.write(str(result))
    # Lire le contenu du fichier texte et le passer à la variable "file_content"
    with open("static/result.txt", "r") as f:
        file_content = f.read()
        # Passer la variable "file_content" à votre template HTML pour l'afficher
    
    print(result)
    print(result)
    return render_template("index.html", result=file_content)


def generate_prompt(animal):
    return animal
    
    
    


if __name__ == "__main__": 

  app.run(host='41.158.213.155')