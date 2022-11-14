from django.contrib.gis import admin
from markers.models import Marker


@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    list_display = ("name", "location")
