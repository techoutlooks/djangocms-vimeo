# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django import forms

from .models import VimeoVideo
from . import settings



class VimeoVideoForm(forms.ModelForm):
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    template = forms.ChoiceField(choices=settings.CMS_VIMEO_TEMPLATES, required=True)
    
    class Meta:
        model = VimeoVideo
        exclude = ('page', 'position', 'placeholder', 'language',
                   'plugin_type')
                   

