from django.contrib import admin
from .models import User, Agent, Social_Account

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Social_Account)
