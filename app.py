from flask import Flask, render_template, Markup, url_for, flash, redirect, request
from datetime import date
app = Flask(__name__)


@app.route('/')
def index():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('index.html')

@app.route('/about_us')
def about_us():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('about_us.html')

@app.route('/cart')
def cart():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('cart.html')

@app.route('/compair')
def compair():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('compair.html')

@app.route('/contact')
def contact():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('contact.html')

@app.route('/footer')
def footer():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('footer.html')

@app.route('/forget_password')
def forget_password():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('forget_password.html')

@app.route('/four_col')
def four_col():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('four-col.html')

@app.route('/general')
def general():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('general.html')

@app.route('/grid_view')
def grid_view():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('grid-view.html')

@app.route('/header')
def header():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('header.html')

@app.route('/list_view')
def list_view():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('list-view.html')

@app.route('/login')
def login():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('login.html')

@app.route('/product_details')
def product_details():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('product_details.html')

@app.route('/products')
def products():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('products.html')

@app.route('/register')
def register():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('register.html')

@app.route('/sidebar')
def sidebar():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('sidebar.html')

@app.route('/three_col')
def three_col():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('three-col.html')




if __name__ == '__main__':
	app.run()
