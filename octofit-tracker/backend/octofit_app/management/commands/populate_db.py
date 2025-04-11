from django.core.management.base import BaseCommand
from octofit_app.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users with superhero themes
        users = [
            User.objects.create(email='thundergod@octofit.edu', name='Thunder God', age=25),
            User.objects.create(email='metalgeek@octofit.edu', name='Metal Geek', age=22),
            User.objects.create(email='zerocool@octofit.edu', name='Zero Cool', age=19),
            User.objects.create(email='crashoverride@octofit.edu', name='Crash Override', age=21),
            User.objects.create(email='sleeptoken@octofit.edu', name='Sleep Token', age=23),
        ]

        # Create teams - using JSONField for members
        blue_team = Team.objects.create(
            name='Blue Team',
            members=[users[0].id, users[2].id, users[4].id]  # Store as list of IDs
        )
        
        gold_team = Team.objects.create(
            name='Gold Team',
            members=[users[1].id, users[3].id]  # Store as list of IDs
        )

        # Create activities
        activities = [
            Activity.objects.create(user=users[0], activity_type='Cycling', duration=60),
            Activity.objects.create(user=users[1], activity_type='Crossfit', duration=120),
            Activity.objects.create(user=users[2], activity_type='Running', duration=90),
            Activity.objects.create(user=users[3], activity_type='Strength', duration=30),
            Activity.objects.create(user=users[4], activity_type='Swimming', duration=75),
        ]

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard.objects.create(user=users[0], score=100),
            Leaderboard.objects.create(user=users[1], score=90),
            Leaderboard.objects.create(user=users[2], score=95),
            Leaderboard.objects.create(user=users[3], score=85),
            Leaderboard.objects.create(user=users[4], score=80),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Cycling Training', description='Training for a road cycling event'),
            Workout.objects.create(name='Crossfit', description='Training for a crossfit competition'),
            Workout.objects.create(name='Running Training', description='Training for a marathon'),
            Workout.objects.create(name='Strength Training', description='Training for strength'),
            Workout.objects.create(name='Swimming Training', description='Training for a swimming competition'),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with OctoFit test data.'))
