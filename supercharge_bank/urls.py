
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',include("bankdets.urls")),
    path('accounts/',include('accounts.urls')),
    path('/internetBanking/',include('internetBanking.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()