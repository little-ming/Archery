from django.urls import include, path
from django.contrib import admin
from common import views
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("sql_api.urls", "sql_api"), namespace="sql_api")),
    path("oidc/", include("mozilla_django_oidc.urls")),
    path("dingding/", include("django_auth_dingding.urls")),
    path("", include(("sql.urls", "sql"), namespace="sql")),
]

if settings.ENABLE_CAS:
    import django_cas_ng.views

    urlpatterns += [
        path(
            "cas/authenticate/",
            django_cas_ng.views.LoginView.as_view(),
            name="cas-login",
        ),
    ]

handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.server_error
