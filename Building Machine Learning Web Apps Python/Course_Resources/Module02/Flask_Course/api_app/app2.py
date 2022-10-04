# Load Core Pkgs

from flask import Flask,render_template,url_for,jsonify

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


# Adding More URL Covert Params
@app.route('/apiroute/<int:mynum>')
def apiroute(mynum):
	return 'The request was:' + str(mynum)

@app.route('/stringroute/<string:mystring>')
def stringroute(mystring):
	return 'The request was:' + mystring


@app.route('/pathroute/<path:mypath>')
def pathroute(mypath):
	return 'The path was:' + mypath




# To Listen on Local Host
if __name__ == '__main__':
	app.run(debug=True)