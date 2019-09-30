from django.contrib import admin
from django.urls import path, include
import blogapp.views
from django.conf import settings
from django.conf.urls.static import static # 미디어파일을 이용하기 위해 임포트



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path('',include('cal.urls')),
    path('home/',include('blogapp.urls')),
    path('board/',include('board.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)