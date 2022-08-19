from flask import Flask,render_template

# init app

app =Flask(__name__)

# Route
@app.route('/')
def index():
    return 'Hello Data Science Optimizers'


# Adding HTML
@app.route('/home')
def home():
    return render_template('home.html')
# Templating

if __name__=='__main__':
    app.run(debug=True)# After developing, do debug=False