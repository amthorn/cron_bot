import flask
import json

import ciscosparkapi

from flask import Flask
from dateutil import parser
from config import LOG_FILE

app = Flask(__name__)

roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vNTA1MDY3YjAtMzM3Zi0xMWU4LThhYmEtMjE3NDEyMGI1ZjU0'  # TEST2
# roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vODQxYmJkMTAtZTI0NS0xMWU2LWE5YmUtNGQxN2YxMzBjNzJk'  # GENERAL

def format_job(string):
    if '::' not in string:
        raise Exception(":: not found in text. Please use :: to separate date and body of message")
    else:
        date, body = [i.strip() for i in string.split("::")]
        date = str(parser.parse(date))

    return date, {'date': date, 'text': body, 'roomId': roomId}

@app.route('/', methods=['POST'])
def index():
    try:
        jobs = json.load(open('log.json', 'r'))
        date, job = format_job(flask.request.form['Body'])
        jobs[date] = job
        json.dump(jobs, open(LOG_FILE, 'w'))
    except Exception as e:
        # text back error
        raise e
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9997, debug=True)