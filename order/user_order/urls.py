from django.urls import path
from .views import ShopViewset, OrderViewset

urlpatterns = [
    path('shop', ShopViewset.as_view({
        'get':'list',
        'post':'create'
    })),
    path('shop/<str:pk>', ShopViewset.as_view({
        'get':'retrieve',
        'put':'upda  te',
        'delete':'destroy'
    })),
    path('order', OrderViewset.as_view({
        'get':'list',
        'post':'create'
    })),
    path('order/<str:pk>', OrderViewset.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
]