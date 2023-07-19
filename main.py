from flask import Flask, jsonify, request, render_template

app = Flask(__name__, '/assets', 'assets')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')













if __name__ == "__main__":
    app.run()