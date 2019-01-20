from flask import Flask
app = Flask(__name__)

"""
Given a list of repositories, given: (# lines of code, # of commented lines, # of stars, # contributors)

Find the: average % commented
"""
@app.route('/begin')
def begin():
    return 'we have begun...'

@app.route('/data')
def data():
    return 'data'
