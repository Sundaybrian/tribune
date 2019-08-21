import datetime as dt
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404



def news_of_day(request):
    date=dt.date.today()
    
    return render(request,'all-news/today-news.html',{'date':date})    

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

    return render(request,'all-news/past-news.html',{'date':date})


