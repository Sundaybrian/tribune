import datetime as dt
from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def news_of_day(request):
    date=dt.date.today()
    day=convert_dates(date)

    html=f'''
    <html>
        <body>
            <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)    

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
    

    day=convert_dates(date)
    html=f'''
    <html>
        <body>
            <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)


