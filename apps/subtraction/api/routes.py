from rest_framework.routers import DefaultRouter

from .viewset import subtraction_log_list_view

router = DefaultRouter()

router.register('', subtraction_log_list_view, basename='sllv')
