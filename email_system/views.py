from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailRecords
from django.db import connection, connections
import report_email_stats


def sendEmail(request):
    if request.method == 'GET':
        report_email_stats.email_report_admin()
        return render(request, 'send_email.html', {})
    if request.method == 'POST':

        cc = request.POST['cc']
        bcc = request.POST['bcc']
        subject = request.POST['subject']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER

        # recipients
        recipients = request.POST['recipients']
        recipient_list = recipients.split(',')
        recipient_list.append('gateway.manish@gmail.com')  # default recipient
        if 'csvfile' in request.FILES:
            csvfile = request.FILES['csvfile']
            if not csvfile.name.endswith('.csv'):
                error_message = 'File is not CSV type. Please upload a CSV file.'
                return render(request, 'send_email.html', {'error_message': error_message})
            elif csvfile.multiple_chunks():
                error_message = "Uploaded file is too big (%.2f MB)." % (csvfile.size / (1000 * 1000),)
                return render(request, 'send_email.html', {'error_message': error_message})
            file_data = csvfile.read().decode("utf-8")
            lines = file_data.split("\n")
            for line in lines:
                email_ids = line.split(",")
            recipient_list.extend(email_ids)

        send_mail(subject, message, email_from, recipient_list)

        # cursor = connections['default'].cursor()
        er = EmailRecords()
        er.subject = subject
        er.recipients = str(recipient_list)
        er.message = message
        er.cc = cc
        er.bcc = bcc
        er.sender = email_from
        er.save()


        return render(request, 'email_sent.html',{})




report_email_stats.start()