from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', universe='Test')
        self.user = User.objects.create(email='test@example.com', username='TestUser', team=self.team, is_leader=True)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, activity_type='Test', duration=10, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, rank=1)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'TestUser')

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

    def test_activity_str(self):
        self.assertIn('TestUser', str(self.activity))

    def test_leaderboard_str(self):
        self.assertIn('Test Team', str(self.leaderboard))
