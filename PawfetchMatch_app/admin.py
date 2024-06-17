from django.contrib import admin
from PawfetchMatch_app.models import *

class ProfileAdmin(admin.ModelAdmin):
  pass

class ListingAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Profile, ProfileAdmin)