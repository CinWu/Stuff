from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return
    
if __name__ == "__main__":
    app.debug = True
    app.run()

    