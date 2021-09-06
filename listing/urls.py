from django.urls import path
from .views import ManageListingView, ListingDetailView, ListingsView


urlpatterns = [
    path('manage', ManageListingView.as_view()),
    path('detail', ListingDetailView.as_view()),
    path('get-listings', ListingsView.as_view()),
]
