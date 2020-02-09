from flask import Flask, render_template

app= Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='sqlite://'
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/saved')
def saved():
   return render_template('saved.html')

@app.route('/post')
def post():
    return render_template('post.html')


if __name__ == '__main__':
    app.run(debug=True)
