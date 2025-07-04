from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not PeriodicTask.objects.filter(name='Daily Market Data Fetch').exists():
            interval = True
            schedule = None
            if interval:
                schedule, _ = IntervalSchedule.objects.get_or_create(
                    every=1,
                    period=IntervalSchedule.MINUTES
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
            # start_time=now()
            self.stdout.write(self.style.SUCCESS('Task to fetch market data created.'))
        else:
            self.stdout.write('Task to fetch market data already exists.')
