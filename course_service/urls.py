from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from courses.views import CourseViewSet, StudentCourseViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('studentcourses', StudentCourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("courses.urls")),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),  # ✅ interface GraphiQL activée
    path("api/ai/", include("ai_service.urls")),

]
