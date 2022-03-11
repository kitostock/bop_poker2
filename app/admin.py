from django.contrib import admin

from .models import (Task, Blog, BopInfo, PersonalCategory,
                     PersonalRate)
from django.contrib.auth import get_user_model

User = get_user_model()


admin.site.register(Blog)
admin.site.register(Task)
admin.site.register(BopInfo)
admin.site.register(PersonalCategory)
admin.site.register(PersonalRate)
