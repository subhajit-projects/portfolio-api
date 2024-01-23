from django.apps import AppConfig


class EmailQueueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_queue'
