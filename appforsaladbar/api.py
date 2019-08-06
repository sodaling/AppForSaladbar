# -*- coding: utf-8 -*-
"""
Programmatic integration point for User API Accounts sub-application
"""

from django.conf import settings
from openedx.core.djangoapps.user_api import errors, helpers
from student.models import (
    User
)

from .serializers import (
    UserReadOnlySerializer, _visible_fields  # pylint: disable=invalid-name
)

# Public access point for this function.
visible_fields = _visible_fields


@helpers.intercept_errors(errors.UserAPIInternalError, ignore_errors=[errors.UserAPIRequestError])
def get_account_settings(request, configuration=None, view=None):
    requesting_user = request.user

    requested_users = User.objects.select_related('profile').all()
    if not requested_users:
        raise errors.UserNotFound()

    serialized_users = []
    for user in requested_users:
        has_full_access = requesting_user.is_staff or requesting_user.username == user.username
        if has_full_access and view != 'shared':
            admin_fields = settings.ACCOUNT_VISIBILITY_CONFIGURATION.get('admin_fields')
        else:
            admin_fields = None
        serialized_users.append(UserReadOnlySerializer(
            user,
            configuration=configuration,
            custom_fields=admin_fields,
            context={'request': request}
        ).data)

    return serialized_users
