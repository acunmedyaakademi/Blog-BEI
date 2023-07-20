from flask import Flask, jsonify, request, render_template
from datetime import datetime
import sqlite3

created_on = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

app = Flask(__name__, '/assets', 'assets')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/all-post')
def all_post():
    blog_data = []
    with sqlite3.connect('blog.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM post')
        row = cursor.fetchall()

        if row is None:
            return "Post not found.", 404

        blog_data = {
            'title': row[2],
            'description': row[3],
        }

    return render_template('post.html', blog_data=blog_data)


@app.route('/post/<int:post_id>')
def post_id(post_id):
    blog_data = []
    with sqlite3.connect('blog.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM post WHERE id = ?', (post_id,))
        row = cursor.fetchone()

        if row is None:
            return "Post not found.", 404

        blog_data = {
            'title': row[2],
            'description': row[3],
            'created_on': row[4]
        }

    return render_template('post.html', blog_data=blog_data)
















@app.route('/contact')
def contact():
    return render_template('contact.html')













if __name__ == "__main__":
    app.run()