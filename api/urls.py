from django.contrib import admin
from django.urls import path, include 
from api.views import *






urlpatterns = [
  path('',get_image),
  path("github",Github.as_view()),
  path("api",api),
  path("fb/api",YoMamaBotView.as_view()),
  path('facebook/api/privacy-policy',privacy_policy_api),
  path('facebook/ia/privacy-policy',privacy_policy_ia)
 ]
