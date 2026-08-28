from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

# Views da nossa aplicação
from core.views import healthcheck
from usuarios.views import CustomTokenObtainPairView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🚦 Infraestrutura
    path('api/v1/healthcheck/', healthcheck, name='healthcheck'),

    # 🔑 Autenticação JWT Customizada (Semana 16)
    path('api/v1/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/logout/', LogoutView.as_view(), name='token_logout'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📚 Apps de Negócio
    path('api/v1/livros/', include('livros.urls')),
    path('api/v1/usuarios/', include('usuarios.urls')),
]