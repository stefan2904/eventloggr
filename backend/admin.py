from django.contrib import admin
from backend.models import *

admin.site.register(Service)
admin.site.register(Endpoint)
admin.site.register(Logline)
admin.site.register(Notifier)

