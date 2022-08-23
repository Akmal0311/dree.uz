from django.urls import path
from .views import *

urlpatterns = [
    path('client/', ClientView.as_view(), name='client'),
    path('client/all/', ClientListView.as_view(), name='client_all'),
    path('region/', RegionView.as_view(), name='region'),
    path('region/<int:pk>', RegionDetailView.as_view(), name='region_detail'),
    path('district/', DistrictView.as_view(), name='district'),
    path('district/<int:pk>', DistrictDetailView.as_view(), name='district_detail'),
    path('tree-type/', TreeTypeView.as_view(), name='tree_type'),
    path('tree-type/<int:pk>', TreeTypeDetailView.as_view(), name='tree_type_detail'),
    path('tree-name/', TreeNameView.as_view(), name='tree_name'),
    path('tree-name/<int:pk>', TreeNameDetailView.as_view(), name='tree_name_detail'),
    path('tree-price/<int:pk>', TreePriceDetailView.as_view(), name='tree_price_detail'),
    path('tree-price/', TreePriceView.as_view(), name='tree_price'),
    path('main_dashboard/', MainDashboardView.as_view(), name='main_dashboard'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('pics/', ClientPics.as_view(), name='client_pics'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('feedback/<int:pk>', FeedbackDetailView.as_view(), name='feedback_detail'),

]

