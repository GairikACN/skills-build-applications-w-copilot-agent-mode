from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    import os
    CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
    base_url = request.build_absolute_uri('/')
    if CODESPACE_NAME:
        base_url = f'https://{CODESPACE_NAME}-8000.app.github.dev/'
    api_base = base_url + 'api/'
    return Response({
        'users': api_base + 'users/',
        'teams': api_base + 'teams/',
        'activities': api_base + 'activities/',
        'leaderboard': api_base + 'leaderboard/',
        'workouts': api_base + 'workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
