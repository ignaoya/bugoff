from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
        #path('',views.index, name='index'),
        path('', views.project_list, name='project_list'),
        path('<str:name>/', views.project_detail, name='project_detail'),
        path('<str:name>/tag/<slug:tag_slug>/', views.project_detail, name='bug_list_by_tag'),
        path('bugs/<str:id>/', views.bug_detail, name='bug_detail'),
        ]
