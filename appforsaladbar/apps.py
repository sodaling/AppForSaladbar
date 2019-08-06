# -*- coding: utf-8
from __future__ import unicode_literals

from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import (
    ProjectType, PluginURLs, PluginSettings, SettingsType
)


class AppforsaladbarConfig(AppConfig):
    name = 'appforsaladbar'
    verbose_name = 'appforsaladbar'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: u'appforsaladbar',
                PluginURLs.REGEX: u'',
            }
        },
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.DEVSTACK: {PluginSettings.RELATIVE_PATH: u'settings.lms_production'},
                SettingsType.AWS: {PluginSettings.RELATIVE_PATH: u'settings.lms_production'},
                SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: u'settings.lms_production'},
            }
        },
    }

