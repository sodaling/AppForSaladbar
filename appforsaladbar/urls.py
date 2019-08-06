# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

ACCOUNTSALADBAR_LIST = views.AccountViewSetSaladbar.as_view({
    'get': 'list',
})

app_name = 'appforsaladbar'
urlpatterns = [
    url(r'', TemplateView.as_view(template_name="base.html")),
    url(
        r'^/api/user/v1/accounts_list$',
        ACCOUNTSALADBAR_LIST,
        name='accounts_detail_api_saladbar'
    ),
]
