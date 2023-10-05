from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/testify")
def testify():
	return render_template("testify.html")

@app.route("/services")
def services():
	return render_template("services.html")

@app.route("/product")
def product():
	return render_template("product.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/order")
def order():
	return render_template("order.html")

@app.route("/animals")
def animals():
	return render_template("animals.html")

@app.route("/farm")
def farm():
	return render_template("farm.html")

if __name__ == "__main__":
	app.run(debug=False,host="0.0.0.0")
