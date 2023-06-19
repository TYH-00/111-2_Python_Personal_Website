from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from mainsite import models       
import random

# Create your views here.

def index(request):
    mynames = ["關艾", "C110134221", "あい"]
    myname = random.choice(mynames)
    return render(request,"index.html",locals())

def nkustnews(request):
    data = models.NKUSTnews.objects.all()
    return render(request, "nkustnews.html", locals())


def all_data(request):
    url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
    r = requests.get(url)
    data = json.loads(r.text)
    bicycle_data = data["retVal"]
    for item in bicycle_data.values():
        new_record = models.HBicycleData(
            sna = item['sna'],
            sbi = int(item['sbi']),
            tot = int(item['tot']))
        new_record.save()
    # 從資料表裡面過濾出我們想要的資料
    data = models.HBicycleData.objects.filter()
    return render(request, "filter.html", locals())

def filtered_data(request):
    # 先刪除所有的舊資料
    models.HBicycleData.objects.all().delete()
    # 先把所有的資料放到資料庫中，比照all_data()中的程式碼
    url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
    r = requests.get(url)
    data = json.loads(r.text)
    bicycle_data = data["retVal"]
    for item in bicycle_data.values():
        new_record = models.HBicycleData(
            sna = item['sna'],
            sbi = int(item['sbi']),
            tot = int(item['tot']))
        new_record.save()
    # 從資料表裡面過濾出我們想要的資料
    data = models.HBicycleData.objects.filter(sbi__gte=10)
    return render(request, "filter.html", locals())

def phonelist(request, id=-1):
    if id==-1:
        data = models.PhoneModel.objects.all()
    else:
        maker = models.PhoneMaker.objects.get(id=id)        #找一個用get
        data = models.PhoneModel.objects.filter(maker=maker) #找好多個，用filter
    return render(request, "phonelist.html", locals())

def chart(request):
    data = models.PhoneModel.objects.all()
    return render(request, "chart.html", locals())

def stock300list(request):
    data = models.StockInfo.objects.filter(price__gte=300).order_by('-price')
    numbers = len(data)
    return render(request, "stocklist.html", locals())




