
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
# from django.template.context_processors import static
from django.urls import path, include

from restasite import views

urlpatterns = [
                  # path('pelmeni', views.pelmeni, name='pelmeni'),
                  # path('pelmeni/<str:category>', views.pelmeni, name='pelmeni'),
                  # path('pelmennaia', views.pelmennaia, name='pelmennaia'),
                  # path('', views.index, name='index'),
                  # path('contact', views.contact, name='contact'),
                  path('', include('restasite.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL,
                       document_root=settings.MEDIA_ROOT)
