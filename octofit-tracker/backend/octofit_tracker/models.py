from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Duration in minutes')
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    total_points = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - Rank {self.rank}"
