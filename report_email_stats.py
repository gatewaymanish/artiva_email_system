from apscheduler.schedulers.background import BackgroundScheduler

def myfunc():
    print('test scheduler')

def start():
    print('scheduler function start() called!')
    scheduler = BackgroundScheduler()
    scheduler.add_job(myfunc, 'interval', minutes=1)
    scheduler.start()