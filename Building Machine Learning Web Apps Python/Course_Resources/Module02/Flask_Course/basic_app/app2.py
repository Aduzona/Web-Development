# Load Core Pkgs

from flask import Flask,render_template

# Init App
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello Data Science Optimizers "

@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	mission = 'Optimizing Data Science'
	return render_template('home.html',data = mission)

# To Listen on Local Host
if __name__ == '__main__':
	app.run(debug=True)