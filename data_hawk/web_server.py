#
# Flask web server
# @author: Hayden McParlane
# @creation-date: 12.12.2015

from flask import Flask
from flask import render_template
import flask
import config

app = Flask(__name__)

@app.route('/', methods=['GET'])
def serve_home():
	'''Serve the home page'''
	return render_template('index.html')
	
if __name__=='__main__':
	app.run(host=config.LOCAL_IP, port=config.LOCAL_PORT, debug=config.RUN_IN_DEBUG)
