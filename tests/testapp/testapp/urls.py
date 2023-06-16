from __future__ import absolute_import, unicode_literals

import wagtail
from django.conf import settings
from django.urls import include, re_path

if wagtail.VERSION >= (2, 0):
    from wagtail.admin import urls as wagtailadmin_urls
    from wagtail.core import urls as wagtail_urls
    from wagtail.documents import urls as wagtaildocs_urls
    from wagtail.images import urls as wagtailimages_urls
else:
    from wagtail.wagtailadmin import urls as wagtailadmin_urls
    from wagtail.wagtailcore import urls as wagtail_urls
    from wagtail.wagtaildocs import urls as wagtaildocs_urls
    from wagtail.wagtailimages import urls as wagtailimages_urls

urlpatterns = [
    re_path(r'^admin/', include(wagtailadmin_urls)),

    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^images/', include(wagtailimages_urls)),

    re_path(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
