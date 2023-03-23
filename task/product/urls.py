from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'accounts', views.UserData,basename="accounts")

# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]


urlpatterns = [
    path('api/', views.ProductData.as_view(), name='api')
]

