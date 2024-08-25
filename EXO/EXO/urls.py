"""EXO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from practice import views
from rest_framework import routers
from api import views

userrouter = routers.DefaultRouter()
userrouter.register(r'User',views.UserViewSet)
cohortrouter = routers.DefaultRouter()
cohortrouter.register(r'cohort', views.CohortViewSet)
cohortinforouter = routers.DefaultRouter()
cohortinforouter.register(r'cohort', views.CohortInfosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('login/',include('login.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('accounts/', include('allauth.urls')),
    path('cohort/',include('cohort.urls')),
    path('cohort/cohortIndex/<cID>',include('cohort.urls'),name='cohortindex'),
    path('cohort/cohortIndex/<cID>/addMember',include('cohort.urls'), name = 'addmembertocohort'),
    path('cohort/cohortIndex/<cID>/createexam',include('cohort.urls'), name = 'addexam'),
    path('cohortIndex/<cID>/examIndex/<eID>', include('cohort.urls')),
    path('cohortIndex/<cID>/examIndex/<eID>/createquestion', include('cohort.urls')),
    ##path('practice/', views.index, name = 'practice'),
    path('rec/', include('core.urls', namespace="core")),
    ##path('exam/',include('exam.urls')),
    ##path('exam/addquestion',include('exam.urls')),
    path('userapi/', include(userrouter.urls)),
    path('cohortapi/', include(cohortrouter.urls)),
    path('cohortinfoapi/', include(cohortinforouter.urls)),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
