from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from reviewer import views

urlpatterns = [
  path('', views.Index.as_view(), name = 'index'),
  path('restaurant/<int:pk>', views.Restaurant.as_view(), name = 'restaurant'),
  path('restaurant/<int:pk>/add_review', views.AddReview.as_view(), name = 'restaurant_review'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
