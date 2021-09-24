from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import json


app = Flask(__name__)


with open('languages.json') as infile:
    language_list = json.load(infile)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        # set the language, use en-US by default
        language = request.form.get('lang') or 'en-US'
        print(f'SELECTED LANGUAGE: {language}')

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)

            # change the line below
            transcript = recognizer.recognize_google(data, language=language)

    return render_template('index.html', transcript=transcript, language_list=language_list)


if __name__ == "__main__":
    app.run(debug=True)