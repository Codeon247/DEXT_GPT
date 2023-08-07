"""dexter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from src.views import StatusView, CreateDexView
from src.views.login import LoginView
from src.views.signup import SignupView
from src.views.query import QueryDexView
from src.views.update import UpdateDexView
from src.views.addprompt import AddPromptView
from src.views.prompts import PromptView
from src.views.instance_status import InstanceStatusView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('status/', StatusView.as_view()),
    path('create/dex/', CreateDexView.as_view()),
    path('dex/status/', InstanceStatusView.as_view()),
    path('query/', QueryDexView.as_view()),
    path('change/prompt/', UpdateDexView.as_view()),
    path('login/', LoginView.as_view(), name='login_view'),
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add/prompt/', AddPromptView.as_view(), name='add_prompt_view'),
    path('prompts/', PromptView.as_view(), name='add_prompt_view'),
]
