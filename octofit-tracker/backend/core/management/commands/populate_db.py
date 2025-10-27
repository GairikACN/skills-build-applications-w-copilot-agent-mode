from django.core.management.base import BaseCommand
from core.models import User, Team, Activity, Leaderboard, Workout
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=[])
        dc = Team.objects.create(name='dc', members=[])

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        for user in users:
            user.save()
        # Update team members after all users are saved
        marvel_members = [user.email for user in User.objects.filter(team='marvel')]
        dc_members = [user.email for user in User.objects.filter(team='dc')]
        Team.objects.filter(name='marvel').update(members=marvel_members)
        Team.objects.filter(name='dc').update(members=dc_members)

        # Create activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2025-10-27')
        Activity.objects.create(user='Captain America', type='swim', duration=45, date='2025-10-26')
        Activity.objects.create(user='Batman', type='cycle', duration=60, date='2025-10-25')
        Activity.objects.create(user='Wonder Woman', type='yoga', duration=50, date='2025-10-24')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=200)
        Leaderboard.objects.create(team='dc', points=180)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Sprints', description='Run 5 sprints', difficulty='medium')
        Workout.objects.create(name='Deadlift', description='Lift heavy weights', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
