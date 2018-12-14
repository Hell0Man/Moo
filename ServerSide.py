import flask
from flask import Flask
app = Flask(__name__)
from flask import request
import dataset


def dbstuff(module, hwid1, name1):
    conn = dataset.connect('sqlite:///auth.db')
    table = conn['AUTH']
    table.insert(dict(HWID=hwid1, Module=module, Name=name1))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form['userk'] == 'Alchemy' and request.form['passwd'] == 'Noob123#':
            hwid = request.form['hwid']
            module = request.form['module']
            name = request.form['name']
            dbstuff(module, hwid, name)
            return 'Success!'
        else:
            return 'False!'
    elif request.method == 'GET':
        return 'Hi'


@app.route('/login', methods=['POST', 'GET'])
def checker():
    if request.method == 'POST':
        if request.form['Kuser'] == 'Coder' and request.form['Kpasswd'] == 'MultiC123':
            hwid = request.form['hwid']
            module = request.form['module']
            conn = dataset.connect('sqlite:///auth.db')
            table = conn['AUTH'].all()
            for entry in table:
                if hwid in entry['HWID'] and module in entry['Module']:
                    return 'Welcome ' + entry['Name']
            return 'No user found!'
    elif request.method == 'GET':
        return 'Hi'


@app.route('/')
def home():
    return 'Hi'


@app.route('/<variable>')
def index(variable):
    return 'Welcome to %s' % variable

