from django.shortcuts import render
from django.urls import reverse_lazy
from livraria_app.models import Book, Author, Category, Publisher
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.utils.translation import gettext_lazy as _


# Create your views here.


def index(request):
    book = Book.objects.all()
    category = Category.objects.all()

    return render(
        request,
        'index.html',
        context={'books': book, 'category': category},
    )


def contact(request):
    return render(
        request,
        'contact.html',
    )


def about(request):
    return render(
        request,
        'about.html',
    )


# author view
class AuthorList(ListView):
    model = Author
    template_name = 'author/list.html'
    context_object_name = 'author'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author/detail.html'
    context_object_name = 'author'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all().filter(authors=self.kwargs['pk'])
        return context


class CreateAuthor(CreateView):
    model = Author
    fields = '__all__'
    exclude = ['slug']
    template_name = 'author/create.html'
    context_object_name = 'author'


class UpdateAuthor(UpdateView):
    model = Author
    exclude = ['slug']
    template_name = 'author/update.html'
    success_url = reverse_lazy('author-list')  # TODO redirect do author detail: reverse_lazy('author-detail')


class DeleteAuthor(DeleteView):
    model = Author
    template_name = 'author/delete.html'
    context_object_name = 'author'
    success_url = reverse_lazy('author-list')  # TODO redirect do author detail: reverse_lazy('author-detail')


# publisher view
class UpdatePublisher(UpdateView):
    model = Publisher
    fields = ['name', 'address', 'city', 'email']
    template_name = 'publisher/update.html'
    success_url = reverse_lazy('publisher-list')  # TODO redirect do publisher detail: reverse_lazy('publisher-detail')


class DeletePublisher(DeleteView):
    model = Publisher
    template_name = 'publisher/delete.html'
    context_object_name = 'publisher'
    success_url = reverse_lazy('publisher-list')


class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'publisher/detail.html'
    context_object_name = 'publisher'


class PublisherList(ListView):
    model = Publisher
    template_name = 'publisher/list.html'
    context_object_name = 'publisher'


class CreatePublisher(CreateView):
    model = Publisher
    fields = '__all__'
    exclude = ['slug']
    template_name = 'publisher/create.html'

    # override form_valid to make sure create_by field is added during the creation of publisher
    # TODO add login required to ensure only logged users can create books
    # @login_required(login_url='/accounts/login/')
    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)


# book view
class UpdateBook(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book/update.html'
    success_url = reverse_lazy('book-list')  # TODO redirect do book detail: reverse_lazy('book-detail')


class DeleteBook(DeleteView):
    model = Book
    template_name = 'book/delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book-list')


class BookDetail(DetailView):
    model = Book
    template_name = 'book/detail.html'
    context_object_name = 'book'


class BookList(ListView):
    model = Book
    template_name = 'book/list.html'
    context_object_name = 'book'


class CreateBook(CreateView):
    model = Book
    fields = '__all__'
    exclude = ['slug']
    template_name = 'book/create.html'

    # override form_valid to make sure create_by field is add during the creation of publisher
    # TODO add login required to ensure only logged users can create books
    # @login_required(login_url='/accounts/login/')
    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)


# category view
class UpdateCategory(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category/update.html'
    success_url = reverse_lazy('category-list')  # TODO redirect do category detail: reverse_lazy('category-detail')


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category-list')


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = 'category'


class CategoryList(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'category'


class CreateCategory(CreateView):
    model = Category
    fields = '__all__'
    exclude = ['slug']
    template_name = 'category/create.html'

    # override form_valid to make sure create_by field is added during the creation of publisher
    # TODO add login required to ensure only logged users can create category
    # @login_required(login_url='/accounts/login/')
    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)

