from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/info")
def home():
    return render_template("info.html")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/")
@app.route("/photos")
def photos():
    return render_template("photos.html")

@app.route("/")
@app.route("/services")
def services():
    return render_template("home.html")
    return "<h1>  home page displaying ...</h1>"

@app.route("/")
@app.route("/contact")
def contact():
    return "<h1> contact page displaying ...</h1>"


@app.route("/contact")
def contact():
    return render_template("contact.html")

# python/templates/.............
# python/templates/home.html   
#jinger elements render to html
if __name__ == '__main__':
    app.run(debug=True, port=8080)