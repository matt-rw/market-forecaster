from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, IntervalSchedule


@receiver(post_migrate)
def setup_periodic_tasks(sender, **kwargs):
    if not PeriodicTask.objects.filter(name='Daily Market Data Fetch').exists():
        interval = True
        schedule = None
        if interval:
            schedule, _ = IntervalSchedule.objects.get_or_create(
                every=1,
                period=IntervalSchedule.DAYS
            )
        else:
            schedule, created = CrontabSchedule.objects.get_or_create(
                minute='0',
                hour='0',
                day_of_week='*',
                day_of_month='*',
                month_of_year='*'
            )
        PeriodicTask.objects.create(
            interval=schedule,
            name='Daily Market Data Fetch',
            task='market.tasks.fetch_market_data'   
        )
        print('test')
        # start_time=now()
