from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def shop_page():
	products = ["detoxifying charcoal mud mask","primRose oil mud mask","calming paper mask"]
	return render_template("shop.html",products = products )

if __name__ == '__main__':
   app.run(debug = True)
