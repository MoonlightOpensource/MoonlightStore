from flask import Flask, render_template, Markup, url_for, flash, redirect, request
from datetime import date
app = Flask(__name__)


@app.route('/')
def index():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('index.html')

@app.route('/')
def about_us():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('about_us.html')

@app.route('/')
def cart():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('cart.html')

@app.route('/')
def compair():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('compair.html')

@app.route('/')
def contact():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('contact.html')

@app.route('/')
def footer():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('footer.html')

@app.route('/')
def forget_password():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('forget_password.html')

@app.route('/')
def four_col():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('four-col.html')

@app.route('/')
def general():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('general.html')

@app.route('/')
def grid_view():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('grid-view.html')

@app.route('/')
def header():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('header.html')

@app.route('/')
def list_view():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('list-view.html')

@app.route('/')
def login():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('login.html')

@app.route('/')
def product_details():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('product_details.html')

@app.route('/')
def products():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('products.html')

@app.route('/')
def register():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('register.html')

@app.route('/')
def sidebar():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('sidebar.html')

@app.route('/')
def three_col():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('three-col.html')




if __name__ == '__main__':
	app.run()
