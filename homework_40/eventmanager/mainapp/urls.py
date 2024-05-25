from django.urls import path
from django.contrib import admin
from . import views

app_name = "mainapp"

urlpatterns = [
    path("", views.index, name="home_page"),
    path("event_details/<int:id>/", views.event_details, name="event_details"),
    path("add_event/", views.add_event, name="add_event"),
    path("delete_event/<int:id>/", views.delete_event, name="delete_event"),
    path("add_attendee_to_event/<int:id>/", views.add_attendee, name="add_attendee"),
    path("delete_attendee/<int:id>/", views.delete_attendee, name="delete_attendee"),
]

admin.site.index_title = "My Site Administration"
admin.site.site_header = "My Site Administration"