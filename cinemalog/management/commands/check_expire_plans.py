from django.core.management.base import BaseCommand, CommandError
from cinemalog.models import UserPlan
from django.utils.timezone import now,timedelta
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        instance=UserPlan.objects.exclude(status=1).order_by('id') #get all active and near to axpire user plans
        for item in instance:  # check one by one
            if item.expire_at<now():
                print(item.user,"you expired already")  # if expire the date
                item.status=1
                item.save()
            elif now()<item.expire_at<now()+timedelta(days=1): #if near to expire the date(less than 24hours)
                print(item.user,"you have less than one day time to expire")
                item.status=2
                item.save()
            elif item.expire_at>now()+timedelta(days=1): #if the date is more than 24H
                print(item.user,"your charge is enough")
