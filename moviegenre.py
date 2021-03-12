from flask import Flask,redirect,request,url_for,render_template,request
app = Flask(__name__)

@app.route(‘/’, methods=[‘GET’, ‘POST’])def main():
    if flask.request.method == ‘GET’:
        return(flask.render_template(‘index.html’))

    if flask.request.method == ‘POST’:
    m_name = flask.request.form[‘movie_name’]
    m_name = m_name.title()