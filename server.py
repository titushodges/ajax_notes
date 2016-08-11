from flask import Flask, render_template, request, redirect, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'notepage')

@app.route('/')
def index():
    query = "SELECT * FROM notes"
    posts = mysql.query_db(query)
    return render_template('index.html', posts = posts)

@app.route('/notes/index_json')
def index_json():
    query = "SELECT * FROM notes"
    posts = mysql.query_db(query)
    return jsonify(posts)

@app.route('/notes/index_html')
def index_html():
    query = "SELECT * FROM notes"
    posts = mysql.query_db(query)
    return render_template('partials/notes.html', posts=posts)

@app.route('/posts/create', methods=['POST'])
def create():
    query = "INSERT INTO notes(title, description, created_at, updated_at) VALUES('{}','{}',NOW(),NOW())".format(request.form['title'], request.form['note'])
    mysql.query_db(query)
    return_query = "SELECT * FROM notes"
    posts = mysql.query_db(return_query)
    return render_template('partials/notes.html', posts=posts)

@app.route('/posts/delete', methods=['POST'])
def delete():
    query = "DELETE FROM notes WHERE id = ('{}')".format(request.form['id'])
    mysql.query_db(query)
    return_query = "SELECT * FROM notes"
    posts = mysql.query_db(return_query)
    return render_template('partials/notes.html', posts=posts)

@app.route('/posts/update', methods=['POST'])
def update():
    query = "UPDATE notes SET description = ('{}') WHERE id = ('{}')".format(request.form['note'], request.form['id'])
    mysql.query_db(query)
    return_query = "SELECT * FROM notes"
    posts = mysql.query_db(return_query)
    return render_template('partials/notes.html', posts=posts)

app.run(debug=True)