from django.http import HttpResponse
from django.shortcuts import render
from article.models import *
from django.core.paginator import Paginator


def test(request):
    return HttpResponse('试一试')


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def listpic(request):
    return render(request, 'listpic.html')


def newslistpic(request, page=1):
    article = Article.objects.order_by('-date')
    paginator = Paginator(article, 6)
    page_obj = paginator.page(int(page))

    current_page = page_obj.number
    start = current_page - 3
    if start < 1:
        start = 0
    end = current_page + 2
    if end > paginator.num_pages:
        end = paginator.num_pages
    if start == 0:
        end = 5
    page_range = paginator.page_range[start:end]

    return render(request, 'newslistpic.html', locals())


def articledetails(request, id):
    article = Article.objects.get(id=int(id))
    return render(request, 'articledetails.html', locals())


def base(request):
    return render(request, 'base.html')


def addarticle(request):
    # for x in range(60):
    # article=Article()
    # article.title='title_%s' % x
    # article.content='content_%s' % x
    # article.description='description_%s' % x
    # article.author=Author.objects.get(id=1)
    # article.save()
    # article.type.add(Type.objects.get(id=1))
    # article.save()
    return HttpResponse('okokokoklllllll')
