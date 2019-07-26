"""
Management command `enabling_TPA` is used to idempotently enable Third Party Authentication.
"""
import logging

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from django.contrib.sites.models import Site
from third_party_auth.models import OAuth2ProviderConfig

LOG = logging.getLogger(__name__)

class Command(BaseCommand):
    # pylint: disable=missing-docstring

    help = 'To enhance sign in options for your users, you can enable third party authentication.'

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('slug')
        parser.add_argument('site')
        parser.add_argument('backend_name')

    @transaction.atomic
    def handle(self, name, slug, site, backend_name, *args, **options):
        """
        It can't be executed before a Site exists.
        """
        set_site = Site.objects.get(name=site, domain=site)
        provider = OAuth2ProviderConfig(name=name)
        provider.slug = slug
        provider.Site = set_site
        provider.enabled = True
        provider.visible = True
        provider.backend_name = backend_name
        provider.save()

        LOG.info("Enable third party authentication for '{site_name}'".format(site_name=set_site.name))
