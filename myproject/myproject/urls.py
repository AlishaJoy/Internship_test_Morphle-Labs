# filepath: /workspaces/Internship_test_Morphle-Labs/myproject/myproject/urls.py
from django.contrib import admin
from django.urls import path
from systeminfo.views import htop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', htop),  # Route for /htop
]