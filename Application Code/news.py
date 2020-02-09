from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy




app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)

class Newspost(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    author = db.Column(db.String(20))
    content = db.Column(db.Text())



@app.route('/')
def index():
   return render_template('index.html')

@app.route('/saved')
def saved():
   return render_template('saved.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    author = request.form['subtitle']
    content = request.form['content']
    return '<h1>Title: {} Author: {} Content: {}</h1>'.format(title,author,content)

if __name__ == '__main__':
    app.run(debug=True)
