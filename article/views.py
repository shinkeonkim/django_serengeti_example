from django.shortcuts import render, get_object_or_404, redirect

from article.models import Article
from .forms import ArticleForm

def new(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            article = form.save(
                commit=False
            )
            article.author = request.user
            article.save()
            
            return redirect('article:show', id=article.id)
  
    return render(request, 'new.html', { 'form': form })


def edit(request, id):
    # 과연 내가 작성한 글만 수정할 수 있는 걸까요?
    article = get_object_or_404(Article, pk=id)
    
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        
        if form.is_valid():
            article = form.save(
                commit=False
            )
            article.save()
            
            return redirect('article:show', id=article.id)
  
    return render(request, 'edit.html', { 'form': form, 'article': article })


def show(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'show.html', { 'article': article })

