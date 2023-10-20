"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.urls import path
# from portal import views

# urlpatterns = [
#     path('', views.indice, name="indice"),
#     path('cursos/', views.cursos, name="cursos")

# ] Esta es la primera forma, pero como voy a crear varias app que manejan varias url, va a ser muy pesado
#Por lo que creo una url.py en cada app y luego la incluyo aca para que asi las pueda referenciar desde mi proyecto}
from django.urls import path, include

urlpatterns = [
    path('', include("portal.urls"))
]
