# here is where we register the different tables we want to show up in the admin panel (this file is not necessary but makes viewing tables easy)
from django.contrib import admin
# import the models from the model file with .models (file path in the same directory)
from .models import VisualCard, User, CommunicationBoard

admin.site.register(VisualCard)
admin.site.register(User)
admin.site.register(CommunicationBoard)
