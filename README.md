djangocms-vimeo
===============

[![Build Status](https://travis-ci.org/nimbis/djangocms-vimeo.svg?branch=master)](https://travis-ci.org/nimbis/djangocms-vimeo)

A [video.js](https://github.com/videojs/video.js) Vimeo video plugin for django CMS.
Loosely based on the [djangocms-video](https://github.com/divio/djangocms-video) plugin.
Uses the [videojs-vimeo](https://github.com/eXon/videojs-vimeo) plugin.


Installation
------------

This plugin requires `django CMS` 3.3.1 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install djangocms-vimeo``.
* Add ``'djangocms_vimeo'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_vimeo``.
* Add your rendering template to CMS_VIMEO_TEMPLATES in your settings.py
```
CMS_VIMEO_TEMPLATES = (
  ('djangocms_vimeo/default.html', _('Default')),
  ('djangocms_vimeo/video.html', _('Video')),
)
```
* Select your template from the plugin's "Advanced Settings" in the CMS.    

Contributing
------------

See the [Contributing Guidelines](CONTRIBUTING.md).

History
-------

v0.4.0:

    * Adding migration required for Django CMS v3.3.1 and later, which is now
      required for this app.  

v0.3.3:

    * Patch the vjs.vimeo.js according to https://github.com/eXon/videojs-vimeo/commit/0543812e2ebe58ed279d695667b4ae9d38029945


v0.3.2:

    * Removing pip requirement from setup.py.


v0.3.0:

    * Upgraded to Video.js v4.9.0. Fixed the broken Django 1.7 migration that existed in v0.2.0.

v0.2.0:

    * Moved existing migrations directory to south_migrations and added Django 1.7 migrations. This version contained a broken Django 1.7 migration.

v0.1.5:

    * Made fixes to videojs-vimeo to correctly detect HTTPS.

v0.1.4:

    * Added missing static directory to MANIFEST.

v0.1.0:

    * Inital release
