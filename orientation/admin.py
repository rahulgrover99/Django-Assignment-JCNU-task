from django.contrib import admin

# Register your models here.
from orientation.models import User, ProjectMentee, Project, ProjectMentor, MentorMentee

admin.site.register(User)
admin.site.register(ProjectMentee)
admin.site.register(ProjectMentor)
admin.site.register(Project)
admin.site.register(MentorMentee)