# Serve Html Content and Jinga Templates
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/journal')
def journal():
    return render_template('journal.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)
