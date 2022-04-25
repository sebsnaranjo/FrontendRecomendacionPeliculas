from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from api.requests_api import RequestsApi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pelicula/<title>')
def reco(title):
    res = RequestsApi.get_api(title)
    print(res)
    return render_template("recomendacion.html", data={"title": title, "recomendacion": res})

if __name__ == '__main__':
    app.run(port=8081, debug=True)