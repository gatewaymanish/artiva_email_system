from django.apps import AppConfig


class EmailSystemConfig(AppConfig):
    name = 'email_system'

    # def ready(self):
    #     import report_email_stats
    #     report_email_stats.start()