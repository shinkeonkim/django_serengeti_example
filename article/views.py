from django.shortcuts import render, get_object_or_404

from article.models import Article

def show(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'show.html', { 'article': article })

