from django.shortcuts import render
from django.views import generic
from  . models import Book
from . forms import BookForm
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class BookListView(generic.ListView):
    queryset = Book.objects.all()
    model = Book
    template_name = 'book_list.html'


def book_create(request):
    data = dict()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('book_list.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    else:
        form = BookForm()

    context = {'form': form}
    data['html_form'] = render_to_string('partial_book_create.html', context, request=request)

    return JsonResponse(data)


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string()





