from django.contrib import admin
from django.contrib.auth.models import User

from .models import LeaveApplication, LeaveBalance, Type_leave
admin.site.register(LeaveApplication)
admin.site.register(LeaveBalance)
admin.site.register(Type_leave)