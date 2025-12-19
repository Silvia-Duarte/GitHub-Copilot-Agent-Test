from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, User, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Super Strength', description='Strength workout')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30, date='2025-12-19')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Spider-Man')
    def test_team_str(self):
        self.assertEqual(str(self.team), 'Marvel')
    def test_activity_str(self):
        self.assertIn('Spider-Man', str(self.activity))
    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Super Strength')
    def test_leaderboard_str(self):
        self.assertIn('Marvel', str(self.leaderboard))

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='DC', description='DC Team')
        self.user = User.objects.create(name='Batman', email='batman@dc.com', team=self.team, is_superhero=True)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)
    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list) or 'results' in response.data)
