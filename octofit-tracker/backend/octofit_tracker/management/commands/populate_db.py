from django.core.management.base import BaseCommand
from octofit_tracker.test_data import TEST_USERS, TEST_TEAMS, TEST_ACTIVITIES, TEST_LEADERBOARD, TEST_WORKOUTS
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        print('Populating users...')
        for user in TEST_USERS:
            print(f"Adding user: {user['email']}")
            User.objects.get_or_create(email=user['email'], defaults={
                'name': user['name'],
                'password': user['password']
            })
        print('Populating teams...')
        for team in TEST_TEAMS:
            print(f"Adding team: {team['name']} with members: {team['members']}")
            t, _ = Team.objects.get_or_create(name=team['name'])
            t.members = team['members']
            t.save()
        print('Populating activities...')
        for activity in TEST_ACTIVITIES:
            print(f"Adding activity for user: {activity['user_email']} type: {activity['activity_type']}")
            user = User.objects.get(email=activity['user_email'])
            Activity.objects.get_or_create(user=user, activity_type=activity['activity_type'], defaults={
                'duration': activity['duration'],
                'date': parse_datetime(activity['date'])
            })
        print('Populating leaderboard...')
        for lb in TEST_LEADERBOARD:
            print(f"Adding leaderboard for team: {lb['team_name']} points: {lb['points']}")
            team = Team.objects.get(name=lb['team_name'])
            Leaderboard.objects.get_or_create(team=team, defaults={'points': lb['points']})
        print('Populating workouts...')
        for workout in TEST_WORKOUTS:
            print(f"Adding workout: {workout['name']}")
            Workout.objects.get_or_create(name=workout['name'], defaults={'description': workout['description']})
        print('Test data populated successfully.')
