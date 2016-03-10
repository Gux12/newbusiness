"""GuXServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from TestModel import views as TestModel_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', TestModel_views.index,name='home'),
    url(r'^delete_musician/$', TestModel_views.delete_musician,name='delete'),
    url(r'^checkall/$', TestModel_views.checkall,name='checkall'),
    url(r'^check/$', TestModel_views.check,name='check'),
]
