# -*-coding: utf-8 -*-
from flask import Flask, send_from_directory, render_template, session, request, redirect, url_for
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    try:
        admin_yn = session['admin']
    except KeyError:
        admin_yn = False

    if request.method == 'GET':
        return """ <form action="index" method="post">
        <input type="text" name="key">
        <input type="submit" value="gogo">"""
    data = request.form['key']
    if data == 'kcronggogo':
        session['admin'] = True
        return redirect(url_for('hello_world'))
    else:
        return redirect(url_for('index'))


@app.route('/jari')
def hello_world():
    if session['admin']:
        pass
    else:
        return redirect(url_for('index'))
    random_our_class = []
    our_class = ['foo', 'bar']

    s = set(range(0, len(our_class)))

    while len(our_class) > 0:
        tmp = random.choice(list(our_class))
        our_class.remove(tmp)
        random_our_class.append(tmp)

    return render_template('index.html',
                           friend=random_our_class)


@app.route('/logout')
def logout():
    session['admin'] = False
    return redirect(url_for('index'))


@app.route('/css/<path:filename>')
def css_static(filename):
    return send_from_directory(app.root_path + '/static/css/', filename)


@app.route('/js/<path:filename>')
def js_static(filename):
    return send_from_directory(app.root_path + '/static/js/', filename)


@app.route('/img/<path:filename>')
def img_static(filename):
    return send_from_directory(app.root_path + '/static/img/', filename)


@app.route('/font/<path:filename>')
def font_static(filename):
    return send_from_directory(app.root_path + '/static/font/', filename)


if __name__ == '__main__':
    app.secret_key = "asdfadfasdf"
    app.run(host='0.0.0.0', debug=True)
