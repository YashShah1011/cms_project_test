from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'user_profiles', UserProfileViewSet)

urlpatterns = router.urls