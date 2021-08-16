from django.contrib import admin

# Register your models here.
from pollapp.models import Survey, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ("question", "ans1", "ans2", "ans3", "ans4", "status")

admin.site.register(Survey, PollAdmin)
admin.site.register(Answer)