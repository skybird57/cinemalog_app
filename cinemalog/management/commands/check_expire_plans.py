from django.core.management.base import BaseCommand, CommandError
from cinemalog.models import UserPlan
from django.utils.timezone import now,timedelta
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        instance=UserPlan.objects.filter(status=0).order_by('id')
        for item in instance:
            if item.expire_at<now():
                print(item.user,"you expired already")
                item.status=1
                item.save()
            elif now()<item.expire_at<now()+timedelta(days=1):
                print(item.user,"you have less than one day time to expire")
                item.status=2
                item.save()
            elif item.expire_at>now()+timedelta(days=1):
                print(item.user,"your charge is enough")
    #    for poll_id in options['poll_ids']:
    #        try:
    #            poll = Poll.objects.get(pk=poll_id)
    #        except Poll.DoesNotExist:
    #            raise CommandError('Poll "%s" does not exist' % poll_id)
    #
     #       poll.opened = False
      #      poll.save()

          #  self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))