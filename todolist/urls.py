from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^tasks/$', views.TaskList.as_view(), name='tasks'),
    url(r'^users/', views.UserList.as_view(), name='users_list'),
    url(r'^register/', views.UserAdd.as_view(), name='registration'),
    url(r'^tasks/update', views.TaskUpdate.as_view(), name='RequestedTasks'),
    url(r'^login/', views.UserLog.as_view(), name='login'),
    url(r'^logout/', views.UserLogout.as_view(), name='logout'),
    url(r'^tasks/add', views.TaskAdd.as_view(), name='addTask'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
