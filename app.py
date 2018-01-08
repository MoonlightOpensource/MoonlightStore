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









if __name__ == '__main__':
	app.run()
