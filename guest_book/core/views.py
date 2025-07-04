from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.views.decorators.http import require_http_methods

from .forms import MyForm

from .models import Message

# Create your views here.



@require_http_methods(["GET", "POST"])
def guests_book_handler(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = MyForm(request.POST)

        if not form.is_valid():
            return HttpResponse(400)

        Message.objects.create(
            name = request.POST.get('name'),
            body = request.POST.get('message')
        )
        return redirect('home')


    else:
        form = MyForm()
        messages = Message.objects.all()

        ctx = {"form": form, "messages": messages}

        return render(request, 'core/home.html', ctx)

