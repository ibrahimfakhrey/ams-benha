from flask import Flask, render_template, redirect, url_for, flash, abort


app = Flask(__name__)
app.config['SECRET_KEY'] ="dasdsada"



@app.route('/')
def home():

    return render_template("index.html")
@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/sports')
def sports():

    return render_template("ams footbal.html")
@app.route('/acadimic')
def acadimic():

    return render_template("acadimic.html")

@app.route('/art')
def art():

    return render_template("art.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
