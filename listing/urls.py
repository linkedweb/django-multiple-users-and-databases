from django.urls import path
from .views import ManageListingView


urlpatterns = [
    path('manage', ManageListingView.as_view()),
]
