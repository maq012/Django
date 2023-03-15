from rest_framework.routers import DefaultRouter

from .viewset import addition_log_list_view

router = DefaultRouter()

router.register('', addition_log_list_view, basename='allv')
