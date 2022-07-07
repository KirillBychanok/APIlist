from django.urls import include, path

from rest_framework import routers

from .views import AdminApiBack, AdminApiSet, GuestApiList, comments

router = routers.SimpleRouter()
router.register(r'ticket', AdminApiSet)
router.register(r'back', AdminApiBack)

urlpatterns = [
    path('api/<int:pk>/comments/', comments),
    path('api/v1/', include(router.urls)),
    path('api/', GuestApiList.as_view()),
]