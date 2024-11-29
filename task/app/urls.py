import django.urls

import app.views

urlpatterns = [
    django.urls.path('', app.views.hello),
]
