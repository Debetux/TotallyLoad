import subprocess
import sys
import urllib.request
import simplejson
import requests

from flask import Flask, flash, redirect, request, render_template, url_for

DEBUG = True
SECRET_KEY = 'this is needed for flash messages'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    print('GOTIT')
    url = request.form['media_url']

    download_link_request = requests.get("http://localhost:9191/api/info?url={}&flatten=True".format(url))
    print(url)
    context = dict()

    context['req'] = simplejson.loads(download_link_request.text)
       
    return render_template('index.html', context = context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8801, debug=True)