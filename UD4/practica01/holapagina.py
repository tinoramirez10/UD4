from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return render_template('hola_pagina.html')

if __name__ == '__main__':
    app.run(debug=True)
