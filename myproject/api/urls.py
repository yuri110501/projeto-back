
from django.urls import path
from .views import ItemListCreateView, ItemDetailView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),  # Lista e cria itens
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),  # Detalha, atualiza e deleta itens
]

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
