import django.http


def hello(request):
    name = request.GET.get('name')
    message = request.GET.get('message')

    return django.http.HttpResponse(f"Hello {name}! {message}!")
