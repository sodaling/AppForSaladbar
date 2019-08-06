# -*- coding: UTF-8 -*-
"""
An API for retrieving user account information.

For additional information and historical context, see:
https://openedx.atlassian.net/wiki/display/TNL/User+API
"""
import logging

from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from openedx.core.lib.api.authentication import OAuth2AuthenticationAllowInactiveUser
from openedx.core.lib.api.parsers import MergePatchParser
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from user_api.errors import UserNotFound

from .api import get_account_settings

log = logging.getLogger(__name__)

USER_PROFILE_PII = {
    'name': '',
    'meta': '',
    'location': '',
    'year_of_birth': None,
    'gender': None,
    'mailing_address': None,
    'city': None,
    'country': None,
    'bio': None,
}


class AccountViewSetSaladbar(ViewSet):
    authentication_classes = (
        OAuth2AuthenticationAllowInactiveUser, JwtAuthentication
    )
    permission_classes = (permissions.IsAdminUser,)
    parser_classes = (MergePatchParser,)

    def list(self, request):
        """
        GET /api/user/v1/accounts_list
        """
        try:
            account_settings = get_account_settings(
                request, view=request.query_params.get('view'))
        except UserNotFound:
            return Response(status=status.HTTP_403_FORBIDDEN if request.user.is_staff else status.HTTP_404_NOT_FOUND)

        return Response(account_settings)
