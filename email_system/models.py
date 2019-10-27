from django.db import models

# Create your models here.




class EmailRecords(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=50, null=False)
    recipients = models.CharField(max_length=500, null=False)
    subject = models.CharField(max_length=200, null=False)
    message = models.CharField(max_length=500, null=True)
    cc = models.CharField(max_length=100, null=True)
    bcc = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'email_records'

    def __str__(self):
        return self.subject + ' ' + str(self.created)

