from django.urls import path, include

app_name = 'weather'

urlpatterns = [
    path('api/', include('weather.api.urls')),
    # ================================================================================
    # For other non api urls
    # path('customer-create/', views.CustomerCreateView.as_view(), name='customer-create'),
    # ================================================================================
]