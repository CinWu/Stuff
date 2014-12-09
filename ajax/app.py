from flask import Flask, render_template, request_url, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('ajax.html')

#go function
@app.route("/getstuff")
def getstuff():
    print "in getstuff"
    print "Returning from getstuff"
    return "returning getstuff"

@app.route("/getslow")
def getstuff():
    print "in getslow"
    time.sleep(10)
    print "Returning from slow"
    return "returning slow"

@app.route("/getfast")
def getstuff():
    print "in getfast"
    time.sleep(5)
    print "Returning from fast"
    return "returning fast"

if __name__ == '__main__':
    app.debug = True
    app.run()

