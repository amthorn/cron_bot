import datetime
import json

from ciscosparkapi import CiscoSparkAPI
from config import LOG_FILE, AVA_KEY
from dateutil import parser


def relax():
    try:
        log = json.load(open(LOG_FILE))
        now = datetime.datetime.now()
        final_log = {}

        for date, job in log.items():
            if (parser.parse(date) - now).total_seconds() <= 0:
                api = CiscoSparkAPI(AVA_KEY)
                api.messages.create(markdown=job['text'], roomId=job['roomId'])
            else:
                final_log[date] = job

        json.dump(final_log, open(LOG_FILE, 'w'))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    relax()