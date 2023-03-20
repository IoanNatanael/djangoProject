from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from userextend.forms import AuthenticationNewForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('intro.urls')),
    path('', include('home.urls')),
    path('', include('student.urls')),
    path('', include('trainer.urls')),
    path('login/', views.LoginView.as_view(form_class=AuthenticationNewForm), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('', include('userextend.urls')),
    path('', include('book.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
