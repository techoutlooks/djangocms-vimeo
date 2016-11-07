# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import VimeoVideoForm
from .models import VimeoVideo
from . import settings


class VimeoVideoPlugin(CMSPluginBase):
    model = VimeoVideo
    name = _("Vimeo Video")
    form = VimeoVideoForm

    render_template = settings.CMS_VIMEO_TEMPLATES[0][0]

    general_fields = [
        'movie_url',
        ('width', 'height'),
        'auto_play',
        'loop',
    ]

    fieldsets = [
        (None, {'fields': general_fields,}),
        ('Advanced Settings', {'fields': ['template']}),
    ]

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template
            
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(VimeoVideoPlugin)
