from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from work_orders import views

urlpatterns = [
    path('work-orders/', views.WorkOrderView.as_view(), name="work-orders"),
    path('work-orders/<int:pk>/', views.WorkOrderDetail.as_view(), name="detail")
]


urlpatterns = format_suffix_patterns(urlpatterns)