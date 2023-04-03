# HeartApp/urls.py created manually
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from HeartApp import views

urlpatterns = [
    path('', views.heart, name='heart'),

]







#  add the following line at the end of the file
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

