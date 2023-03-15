from rest_framework.routers import DefaultRouter

from .viewset import multiply_log_list_view

router = DefaultRouter()

router.register('', multiply_log_list_view, basename='mllv')
