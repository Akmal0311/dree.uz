from django.urls import path
from .views import *

urlpatterns = [
    path('client/', ClientView.as_view(), name='client'),
    path('tree-price/', TreePriceView.as_view(), name='tree_price'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
]
