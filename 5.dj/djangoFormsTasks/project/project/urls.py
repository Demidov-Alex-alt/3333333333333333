from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delivery/', include('deliveryform.urls')),
    path('news/', include('newsposts.urls')),
]