from flask import Flask, render_template, Markup, url_for, flash, redirect, request
from datetime import date
app = Flask(__name__)


@app.route('/')
def index():
	context = {"page_title": "Moonlight Store", "current_year": date.today().year}
	return render_template('index.html')




if __name__ == '__main__':
	app.run()
