import datetime as dt
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to moringa tribune')

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

