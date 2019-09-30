from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.posthome, name='posthome'),
    path('new', views.postnew, name='postnew'),
    path('create', views.postcreate, name='postcreate'),
    path('show/<int:post_id>', views.postshow, name='postshow'),
    path('edit/<int:post_id>', views.postedit, name='postedit'),
    path('update/<int:post_id>', views.postupdate, name='postupdate'),
    path('delete/<int:post_id>', views.postdelete, name='postdelete'),
    path('comentcreate/<int:post_id>',views.commentcreate,name='commentcreate'),
    path('commentdelete/<int:post_id>/<int:comment_id>',views.commentdelete,name="commentdelete"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
