

from django.contrib import admin
from django.urls import path
from speakers import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('speakers/', views.speaker_list, name='speaker_list'),
path('speakers/create/', views.speaker_create, name='speaker_create'),
path('speakers/<int:speaker_id>/', views.speaker_read, name='speaker_ read'),
path('speakers/<int:speaker_id>/update/', views.speaker_update, name='speaker_update'),
path('speakers/<int:speaker_id>/delete/', views.speaker_delete, name='speaker_delete'),
]


