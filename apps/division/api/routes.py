from rest_framework.routers import DefaultRouter

from .viewset import division_log_list_view
router = DefaultRouter()

router.register('', division_log_list_view, basename='dllv')
