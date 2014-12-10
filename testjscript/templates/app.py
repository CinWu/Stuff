from flask import Flask, render_template, request_url, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

