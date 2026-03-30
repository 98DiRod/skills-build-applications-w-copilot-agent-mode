from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', username='IronMan', team=marvel, is_leader=True)
        steve = User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', username='Batman', team=dc, is_leader=True)
        clark = User.objects.create(email='clark@kent.com', username='Superman', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Do 50 pushups', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Run 5km', difficulty='Medium')
        squats = Workout.objects.create(name='Squats', description='Do 40 squats', difficulty='Easy')

        # Create Activities
        Activity.objects.create(user=tony, activity_type='Pushups', duration=10, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='Squats', duration=15, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Running', duration=25, date=timezone.now().date())

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=200, rank=1)
        Leaderboard.objects.create(team=dc, total_points=150, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
