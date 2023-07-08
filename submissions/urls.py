from django.urls import path
from reddit import views

urlpatterns = [
    # other URL patterns...
    path('submission/<int:submission_id>/', views.submission_detail, name='submission_detail'),
    # other URL patterns...
]
