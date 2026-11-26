from django.urls import path
from .views import JobListView, JobDetailsView


urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),

    path(
        'jobs/<int:pk>/',
        JobDetailsView.as_view(),
        name='job-details'
    ),
]
