from django.contrib import admin
from django.urls import path, include, re_path
from accounts.views import home
from django.conf import settings
from django.conf.urls.static import static

from chat.views import index
from put_calendar.api.router import router
from put_calendar.views import *

from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assignments/', include('assignments.urls')),
    path('notifications/', include('notifications.urls')),
    path('clients/', include('clients.urls')),
    path('accounts/', include('accounts.urls')),
    path('history/', include('history.urls')),
    path('', home, name='home'),
    path('blog/', include('blog.urls')),
    path('calendar/', include('put_calendar.urls')),
    path('chat/', include('chat.urls')),
    path('api/posts/', include('blog.api.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

    re_path(r'^api/dates/$', DatesListView.as_view()),
    re_path(r'^api/dates/(?P<pk>\d+)/$', DatesView.as_view()),
    re_path(r'^api/user/$', UserListView.as_view()),
    re_path(r'^api/user/(?P<pk>\d+)/$', UserView.as_view()),
    re_path(r'^api/filter/(?P<pk>\d+)/$', DatesFilterView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
