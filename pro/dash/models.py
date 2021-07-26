from django.db import models

# Create your models here.


complaint_regard = [
    ('Admission', 'Admission'),
    ('Finance', 'Finance'),
    ('Examination', 'Examination'),
    ('Learning', 'Learning')
]

choices = [
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('MEC', 'MEC'),
    ('EEE', 'EEE'),
    ('CIV', 'CIV'),
    ('AUTO', 'AUTO'),
]


class Complaint(models.Model):
    cid = models.AutoField(primary_key = True)
    name = models.fields.CharField(max_length=100)
    email = models.fields.EmailField(max_length=1000)
    branch = models.fields.CharField(max_length=100,choices= choices, default='cse')
    complaint_regarding = models.fields.CharField(max_length=30, choices=complaint_regard, default='admission')
    complaint_message = models.fields.TextField(max_length=1000)
    status = models.fields.CharField(max_length=1000, default="Complaint Registered")

    def __str__(self):
        return str(self.cid)
