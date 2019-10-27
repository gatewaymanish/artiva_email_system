from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from email_system.models import EmailRecords
from django.core.mail import send_mail
from django.conf import settings



def email_report_admin():
    admins = User.objects.filter(is_superuser=1)
    er = EmailRecords.objects.filter( created__lt = datetime.now(), created__gte = datetime.now() - timedelta(minutes = 30) )

    recipient_list = []
    for item in admins:
        recipient_list.append(item.email)

    message = '\n\nEmail records of last 30 minutes.\n'
    if len(er) > 0:
        for email in er:
            message += 'Subject: ' + str(email.subject) + ', Time: ' + str(email.created.strftime("%m/%d/%Y, %H:%M:%S")) + '\n'
    else:
        message = 'No email records found for last 30 minutes'
    subject = 'Email stats of last 30 minutes.'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)
    print('Email report sent to admin at ',datetime.now())




def start():
    print('scheduler function start() called!')
    scheduler = BackgroundScheduler()
    scheduler.add_job(email_report_admin, 'interval', minutes=30)
    scheduler.start()