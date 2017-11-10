from django.shortcuts import render
from post.models import *
from django.core.paginator import Paginator, Page, EmptyPage, InvalidPage
from django.shortcuts import HttpResponse, HttpResponseRedirect
from haystack.query import SQ, SearchQuerySet
from haystack.models import SearchResult
# Create your views here.


# display index.html and paginate
def index_view(request,num=1):
    # page number
    num = int(num)
    # the number of per page post
    per_page = 1
    paginator = Paginator(Post.objects.order_by('-modifiedTime').all(), per_page)

    # check validity
    if num < 1:
        num = 1
    if num > paginator.num_pages:
        num = paginator.num_pages

    # get content of the num page
    page = paginator.page(num)

    # get the range about display in web and check validity
    previous = 2
    last = 2
    start = num - previous
    end = num + last
    if start <= 0:
        start = 1
        end = previous + last + 1
    if end > paginator.num_pages:
        end = paginator.num_pages
        start = end - previous - last
        if start <=0 :
            start = 1

    return render(request, 'index.html', context={'page': page, 'page_range': range(start, end+1)})


# display post details
def post_details_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Exception as err:
        print(str(err))
    return render(request, 'details.html', {'post': post})


# display about me
def about_view(request):
    content = About.objects.first()
    return render(request, 'about.html', {'content': content})


# display archive by category
def category_details_view(request, category_id=None):
    posts = Post.objects.filter(category=category_id).order_by('-createdTime')
    return render(request, 'archive.html', {'posts': posts})


# display archive by date
def date_details_view(request, year=None, month=None):
    if (year is None) and (month is None):
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(createdTime__year=year, createdTime__month=month)
    return render(request, 'archive.html', {'posts': posts})


# display archive by tag
def tag_details_view(request, tag_id):
    # query posts when the posts have the same tag id
    tag_name = Tag.objects.filter(id=tag_id)[0].name
    posts = Post.objects.filter(tags__name__contains=tag_name)

    return render(request, 'tags.html', {'posts': posts})


def search_view(request):
    print('执行')
    # get search keyword
    keyword = request.GET.get('keyword')
    paginator = Paginator(SearchQuerySet().filter(SQ(title=keyword) | SQ(content=keyword)).all(), per_page=10)
    page = paginator.page(1)

    posts = []
    for result in page.object_list:
        posts.append(result.object)
    return render(request, 'archive.html', {'posts': posts})
