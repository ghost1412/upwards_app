from django.contrib import admin
from request_logger import models as exception_log_models

admin.site.register(exception_log_models.DBLogEntry)
admin.site.register(exception_log_models.GeneralLog)
