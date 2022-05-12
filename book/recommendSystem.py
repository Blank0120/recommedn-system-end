from django.http import HttpResponse
import json

#本文件与其高度耦合， 当作一个文件即可
from graduationProject import *

os.environ["PYSPARK_PYTHON"] = "F:/Python/pythonC38/python"
os.environ["SPARK_HOME"] = "F:/Python/pythonC38/Lib/site-packages/pyspark"


def get_top_rating(request):
    print("recommend_get_top_ratings")
    uid = request.GET.get('uid')
    uid = int(uid)
    print(uid)
    recommend_top_json = get_top_ratings(uid)

    return HttpResponse(json.dumps(recommend_top_json), headers={"Access-Control-Allow-Origin": "*"})


from  book.serializers import book
from django.core import serializers


def search_book(request):
    print("search_book")
    keyword = request.GET.get('keyword')
    print(keyword)
    json = serializers.serialize("json", book.objects.filter(BookTitle__contains=keyword)[:50])
    return HttpResponse(json)

def get_book_detail(request):
    print("get_book_detail")
    isbn = request.GET.get('isbn')
    print(isbn)
    json = serializers.serialize("json", book.objects.filter(ISBN__exact=isbn))
    return HttpResponse(json)

def get_ratings(request):
    print("get_ratings...")
    top_json = serializers.serialize("json",book.objects.order_by("rate")[:50])
    return HttpResponse(json.dumps(top_json), headers={"Access-Control-Allow-Origin": "*"})




