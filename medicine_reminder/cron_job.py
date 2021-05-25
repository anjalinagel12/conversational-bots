from datetime import datetime
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from pytz import timezone

import os
from twilio.rest import Client


def task():
    """
    perform the task we wanted
    :return:
    """
    print("====ANJALI HERE=====")

    # Download the helper library from https://www.twilio.com/docs/python/install


    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'AC4e44a779f86172f353f64a2ffdb7f4ea'
    auth_token = '46d9344eeed4ce019ff8768680c23a69'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body='Hi, its time to take your medicine. Please take it now and take care :)',
            from_='+14159434955',
            to='+919945313337'
        )

    print(message.sid)
    print("task ended")
    print("==========")


def initiate_background_task(time="night"):
    scheduler = BackgroundScheduler()
    ist_timezone = timezone('Asia/Kolkata')
    if time == 'night':
        hour=12 + 8
        minute=30
        second=0
    elif time == 'afternoon':
        hour=12 + 1
        minute=30
        second=0
    else:
        hour=0 + 8
        minute=30
        second=0

    print("initiating back ground task at - ",hour,":",minute,":",second)


    ct = CronTrigger(hour=hour, minute=minute, second=second, timezone=ist_timezone)
    scheduler.add_job(task, ct)
    scheduler.start()
    print("background task initiation is done")


if __name__ == "__main__":
    # autorun
    print("starting autorun program")
    initiate_background_task('night')
    print("going to infinite sleep")
    SLEEP_TIME = 3600
    while True:
        sleep(SLEEP_TIME)
