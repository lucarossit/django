from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from news.models import News
from .forms import NewsForm

def news(request):
    news_objs = News.objects.filter()
    context = {
        "allNews": news_objs,
    }

    return render(request, "news.html", context)

@login_required
def editNews(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save()
            return redirect('news')
    else:
        form = NewsForm(instance=news)
    return render(request, 'editNews.html', {'form': form})

@login_required
def newNews(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('news')
    else:
        form = NewsForm()
    return render(request, 'newNews.html', {'form': form})

@login_required
def deleteNews(request, pk):
    News.objects.filter(pk=pk).delete()
    return redirect('news')