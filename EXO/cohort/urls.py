from django.urls import include
from django.urls import path
from . import views
urlpatterns = [
    path('',views.addCohort),
    path('cohortIndex/<cID>',views.cohortIndex),
    path('cohortIndex/<cID>/addMember/', views.addMember),
    path('cohortIndex/<cID>/createexam/', views.createExam),
    path('cohortIndex/<cID>/examIndex/<eID>/', views.examIndex),
    path('cohortIndex/<cID>/examIndex/<eID>/createquestion/', views.createQuestion),
    
]