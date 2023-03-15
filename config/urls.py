from django.contrib import admin
from django.urls import path, include
from apps.addition.api import urls as addition_urls
from apps.subtraction.api import urls as subtraction_urls
from apps.multiplication.api import urls as multiplication_urls
from apps.division.api import urls as division_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/addition', include(addition_urls)),
    path('app/subtraction', include(subtraction_urls)),
    path('app/multiplication', include(multiplication_urls)),
    path('app/division', include(division_urls)),
    # path('tutorials_details/<int:id>', tutorials_details)
]
