from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.create_order, name='create_order'),
    path('orders/<int:order_id>/', views.get_order, name='get_order'),
    path('orders/<int:order_id>/update/', views.update_order, name='update_order'),
    path('orders/<int:order_id>/delete/', views.delete_order, name='delete_order'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  
]


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from api.views import ItemViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="My Project API",
        default_version='v1',
        description="Documentação da API do meu projeto",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger
]
