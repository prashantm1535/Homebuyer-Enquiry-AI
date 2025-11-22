from django.urls import path
from .views import HomeView, PredictView, InsightsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('predict/', PredictView.as_view(), name='predict'),
    path('insights/', InsightsView.as_view(), name='insights'),
]
