from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts import views

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'accounts', views.UserData,basename="accounts")

# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]


urlpatterns = [
    path('api/', views.UserData.as_view(), name='api'),
    path('get_info/', views.GetUSerList.as_view(), name='get_info'),
    path('user_cart/', views.UserCart.as_view(), name='get_info'),

    
]
