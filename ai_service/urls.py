from django.urls import path
from .views import translate_text, summarize_text

urlpatterns = [
    path("translate/", translate_text),
    path("summarize/", summarize_text),
]
