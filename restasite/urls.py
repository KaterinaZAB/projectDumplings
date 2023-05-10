from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from restasite import views

app_name = 'restasite'
urlpatterns = [
              path('', views.index, name='index'),
              path('pelmeni', views.pelmeni, name='pelmeni'),
              path('pelmeni/<str:category>', views.pelmeni, name='pelmeni'),
              path('pelmennaia', views.pelmennaia, name='pelmennaia'),
              path('contact', views.contact, name='contact'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL,
              document_root=settings.MEDIA_ROOT)
