# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path

from store import views

urlpatterns = [
    path('store/',views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
