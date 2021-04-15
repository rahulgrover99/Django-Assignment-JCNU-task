from django.db import models


# Create your models here.
from django.utils.timezone import now


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Project(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class ProjectMentor(models.Model):
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, default=1)
    mentor_id = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)


class ProjectMentee(models.Model):
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, default=1)
    mentee_id = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)


class MentorMentee(models.Model):
    mentor_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='mentorReverse', default=1)
    mentee_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='menteeReverse', default=1)
