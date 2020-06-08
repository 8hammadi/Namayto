from django.contrib import admin
from django.urls import path, include 
from api.views import *






urlpatterns = [
  path('',home),
  path('signin-facebook',home),
  path("github",Github.as_view()),
  path("api",api),
  path("fb/testapi",YoMamaBotViewTest.as_view()),
  path("fb/api",YoMamaBotView.as_view()),
  path('facebook/api/privacy-policy',privacy_policy_api),
  path('facebook/ia/privacy-policy',privacy_policy_ia)
 ]
