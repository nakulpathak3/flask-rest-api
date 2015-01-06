#!flask/bin/python
from flask import Flask

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Learn REST APIs',
        'description': u'Understand and build RESTful services.',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Finish book learn python the hard way',
        'done': False
    }
]

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)


