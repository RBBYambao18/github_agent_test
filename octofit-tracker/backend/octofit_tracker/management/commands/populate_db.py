from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel.name)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc.name)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc.name)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2025-10-28')
        Activity.objects.create(user=batman, type='Cycling', duration=45, date='2025-10-28')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        # Create workouts
        Workout.objects.create(name='Push Ups', description='Upper body workout', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Lower body workout', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
