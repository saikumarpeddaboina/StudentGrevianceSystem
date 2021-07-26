from django.db import models
from django.contrib.auth.models import User

choices = [
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('MEC', 'MEC'),
    ('EEE', 'EEE'),
    ('CIV', 'CIV'),
    ('AUTO', 'AUTO'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.fields.CharField(choices=choices, default='cse',max_length=30)
    is_head = models.fields.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Profile"
