from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.order_by('-date')
    # news = Articles.objects.order_by('-date')[:2]
    return render(request, 'news/news_home.html', {'news': news})


# После url попадаем в функцию, а оттуда в шаблон, а оттуда в условие повыше
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()
    context = {'form': form, 'error': error}
    return render(request, 'news/create.html', context)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    # fields = ['title', 'anons', 'full_text']
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'
