from django.contrib import admin
from rms import models

from opal.admin import EpisodeSubrecordAdmin

admin.site.unregister(models.ReferralDetails)

class ReferralDetailsAdmin(EpisodeSubrecordAdmin):
    list_display = ['__unicode__', 'when', 'who']

admin.site.register(models.ReferralDetails, ReferralDetailsAdmin)
admin.site.register(models.ClinicLocation)
