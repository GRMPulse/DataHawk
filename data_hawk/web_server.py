#
# Flask web server
# @author: Hayden McParlane
# @creation-date: 12.12.2015

from flask import Flask
from flask import render_template
import flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	'''Serve the home page'''
	return render_template('index.html')
	

if __name__=='__main__':
	app.run(host='159.203.246.108', port=5000, debug=False)
