import os
from celery import Celery
from celery.schedules import crontab

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Create Celery app
app = Celery('backend')

# Load settings from Django settings file, using 'CELERY_' prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()

# Define Celery Beat schedule
app.conf.beat_schedule = {
    'fetch-stock-every-15-minutes': {
        'task': 'stockapp.tasks.fetch_stock_data',
        'schedule': crontab(minute='*/15'),
    },
}
