from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("courses.urls")),  # ✅ Routes pour les cours
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    
  
]