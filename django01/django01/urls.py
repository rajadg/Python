"""django01 URL Configuration

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

from application import index

from application.simple import samples, database, mailer

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index.index_page),
    url(r'^index', index.index_page),
    url(r'^simple_template', index.simple_template),
    url(r'^bootstrap_template', index.bootstrap_template),
    url(r'^simple/welcome', samples.welcome_page),
    url(r'^simple/json', samples.json_formatter),
    url(r'^simple/contacts', database.contact_view),
    url(r'^simple/send_mail', mailer.compose_email),
]


index.all_urls["patterns"] = urlpatterns
