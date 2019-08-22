import datetime as dt
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Article



def news_of_day(request):
    date=dt.date.today()
    news=Article.todays_news()
    
    return render(request,'all-news/today-news.html',{'date':date,'news':news})    

def convert_dates(dates):
    '''
    Function that returns day of the week
    '''
    #get weekday number 
    day_number=dt.date.weekday(dates)

    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #Returning the actual day of the week
    day=days[day_number]
    return day  

def past_days_news(request,past_date):

    try:
        #converts data from the string url
        date=dt.datetime.strptime(past_date,'%Y-%m-%d').date()
        
    except ValueError:
        #Raise 404 error from the string url
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_of_day)    

    news=Article.days_news(date)    

    return render(request,'all-news/past-news.html',{'date':date,'news':news})


def search_results(request):
    '''
    view function that fetches articles based on search terms
    '''  

    if 'article' in request.GET and request.GET["article"]:
        search_term=request.GET.get('article')
        search_articles=Article.search_by_title(search_term)
        message=f"{search_term}"

        return render(request,'all-news/search.html',{'message':message,"articles":search_articles})

    else:
        message='You havent searched for any term'
        return render(request,'all-news/search.html',{'message':message})    
  

def article(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return render (request,"all-news/article.html",{"article":article})          


