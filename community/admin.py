from django.contrib import admin
from community.models import Discipline, ResearchEstablishment, ResearchField, UserProfile


admin.site.register(UserProfile )
admin.site.register(Discipline)
admin.site.register(ResearchField)
admin.site.register(ResearchEstablishment)