from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tarefas.api_rest.views import TarefaViewSet

router = DefaultRouter()
router.register(r'', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
