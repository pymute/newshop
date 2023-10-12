from django.urls import path
from .views import ListApiView,CreateApiView,DetailApiView,UpdateApiView

urlpattern = [

    path('',ListApiView.as_view),
    path('detail/',DetailApiView.as_view),
    path('create/',CreateApiView.as_view),
    path('update/',UpdateApiView.as_view)
]