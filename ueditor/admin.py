#coding:utf-8
"""EntryAdmin for zinnia-ckeditor"""
from django import forms
from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from zinnia.models import Entry
from zinnia.admin.entry import EntryAdmin
from zinnia.admin.forms import EntryAdminForm
from zinnia.settings import ENTRY_BASE_MODEL
from .widgets import UEditorWidget

# if 'ckeditor_uploader' in settings.INSTALLED_APPS:
    # from ckeditor_uploader.widgets import CKEditorUploadingWidget as CKEditor
# else:
    # from ckeditor.widgets import CKEditorWidget as CKEditor


# CONFIG_NAME = 'zinnia-content'
# CKEDITOR_CONFIG = getattr(settings, 'CKEDITOR_CONFIGS', {})
# if CONFIG_NAME not in CKEDITOR_CONFIG:
    # CONFIG_NAME = 'default'


class EntryAdminUEditorForm(EntryAdminForm):
    """
    Define the CKEditor widget for the content field.
    """
    content = forms.CharField(
        label=_('Content'), required=False,
        widget=UEditorWidget())#(config_name=CONFIG_NAME))


class EntryAdminUEditorMixin(object):
    """
    Mixin adding CKEditor for editing Entry.content field.
    """
    form = EntryAdminUEditorForm


class EntryAdminUEditor(EntryAdminUEditorMixin,
                         EntryAdmin):
    """
    Enrich the default EntryAdmin with CKEditor.
    """
    pass


if ENTRY_BASE_MODEL == 'zinnia.models_bases.entry.AbstractEntry':
    admin.site.unregister(Entry)
    admin.site.register(Entry, EntryAdminUEditor)
