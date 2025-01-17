from __future__ import unicode_literals

from django.conf.urls import include
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.i18n import set_language
from django.contrib.auth import views as auth_views

import debug_toolbar

from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings

from katika.views import home, about
#import eseka


admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = i18n_patterns(
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    path("admin/", include(admin.site.urls)),
    path("admin/password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("admin/password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
)

if settings.USE_MODELTRANSLATION:
    urlpatterns += [
        path('i18n/', set_language, name='set_language'),
    ]

urlpatterns += [
    # We don't want to presume how your homepage works, so here are a
    # few patterns you can use to set it up.

    # HOMEPAGE AS STATIC TEMPLATE
    # ---------------------------
    # This pattern simply loads the index.html template. It isn't
    # commented out like the others, so it's the default. You only need
    # one homepage pattern, so if you use a different one, comment this
    # one out.

    # path("^$", direct_to_template, {"template": "index.html"}, name="home"),

    # HOMEPAGE AS AN EDITABLE PAGE IN THE PAGE TREE
    # ---------------------------------------------
    # This pattern gives us a normal ``Page`` object, so that your
    # homepage can be managed via the page tree in the admin. If you
    # use this pattern, you'll need to create a page in the page tree,
    # and specify its URL (in the Meta Data section) as "/", which
    # is the value used below in the ``{"slug": "/"}`` part.
    # Also note that the normal rule of adding a custom
    # template per page with the template name using the page's slug
    # doesn't apply here, since we can't have a template called
    # "/.html" - so for this case, the template "pages/index.html"
    # should be used if you want to customize the homepage's template.
    # NOTE: Don't forget to import the view function too!

    # path("^$", mezzanine.pages.views.page, {"slug": "/"}, name="home"),
    # path("^busted", busted, name="busted"),#, {"slug": "/"}, name="home"),
    #path("^eseka/", include("eseka.urls")),

    path('', home, name='home'),
    path('anycluster/', include('anycluster.urls')),
    path('incident/', include('incident.urls')),
    path('kthesis/', include('kthesis.urls')),
    #path('^khistory/', include('khistory.urls')),
    path('about/', about, name='about'),

    path('blog/', include('kblog.urls')),
    path('jailed/', include('jailed.urls')),
    path('covid19/', include('covid19.urls')),
    path('transcribe/', include('transcribe.urls')),
    path('tender/', include('tender.urls')),
    path('budget/', include('budget.urls')),


    ## User mgnmt, signup, login, logout
    # https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),  # <--

    path("__debug__/", include(debug_toolbar.urls)),


    # HOMEPAGE FOR A BLOG-ONLY SITE
    # -----------------------------
    # This pattern points the homepage to the blog post listing page,
    # and is useful for sites that are primarily blogs. If you use this
    # pattern, you'll also need to set BLOG_SLUG = "" in your
    # ``settings.py`` module, and delete the blog page object from the
    # page tree in the admin if it was installed.
    # NOTE: Don't forget to import the view function too!

    # path("^$", mezzanine.blog.views.blog_post_list, name="home"),

    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

    # If you'd like more granular control over the patterns in
    # ``mezzanine.urls``, go right ahead and take the parts you want
    # from it, and use them directly below instead of using
    # ``mezzanine.urls``.
    #path("", include("mezzanine.urls")),

    # MOUNTING MEZZANINE UNDER A PREFIX
    # ---------------------------------
    # You can also mount all of Mezzanine's urlpatterns under a
    # URL prefix if desired. When doing this, you need to define the
    # ``SITE_PREFIX`` setting, which will contain the prefix. Eg:
    # SITE_PREFIX = "my/site/prefix"
    # For convenience, and to avoid repeating the prefix, use the
    # commented out pattern below (commenting out the one above of course)
    # which will make use of the ``SITE_PREFIX`` setting. Make sure to
    # add the import ``from django.conf import settings`` to the top
    # of this file as well.
    # Note that for any of the various homepage patterns above, you'll
    # need to use the ``SITE_PREFIX`` setting as well.

    # ("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls"))

]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
#handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
