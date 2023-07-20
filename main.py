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


@app.route('/post')
def post():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM post')
    rows = cursor.fetchall()
    blog_data = []
    for row in rows:
        blog_data.append({
            'id': row[0],
            'post_id': row[1],
            'title': row[2],
            'description': row[3],
            'created_on' : row[4]
        })
    conn.close()
    return render_template('post.html',blog_data=blog_data)



    




@app.route('/contact')
def contact():
    return render_template('contact.html')













if __name__ == "__main__":
    app.run()