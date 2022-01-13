from django.urls import path
from django.views.generic import RedirectView

from webapp.models import IssueTracker
from webapp.views import (
    IndexView,
    IssueTrackerView,
    CreateIssueTrackerView,
    IssueTrackerUpdateView,
    IssueTrackerDeleteView)

urlpatterns = [
    path('', IndexView.as_view),
    path('articles/add/', CreateIssueTrackerView.as_view(),
    path('article/<int:pk>/', IssueTrackerView.as_view(template_name = "issue_tracker_view.html"),
    path('article/<int:pk>/update', IssueTrackerUpdateView.as_view(),
    path('article/<int:pk>/delete', IssueTrackerDeleteView.as_view(),
]

