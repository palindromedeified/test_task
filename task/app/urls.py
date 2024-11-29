import django.urls

import task.app.views

urlpatterns = [
    django.urls.path('', task.app.views.hello),
]
