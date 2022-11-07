from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered




############ register all app in admin site ############
app_models = apps.get_app_config('product').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass