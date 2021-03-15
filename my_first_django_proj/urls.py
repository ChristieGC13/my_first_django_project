# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('first_app.routes')),
    # path('admin/', admin.site.urls),
]
