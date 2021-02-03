from django.shortcuts import render
import numpy as np
# Create your views here.
from django.shortcuts import HttpResponse 
import pandas as pd 
import json 
  

def Table(request): 
    used_features = ['Timestamp','Close','EMAV5','Vol','EMAVVol5','MACD13','EMAVMACD5','RSI14']
    df = pd.read_csv("Set50_20190830_20200317_1minute.csv",usecols =used_features,encoding= 'unicode_escape')
    df.set_index("Timestamp",inplace=True)
    json_records = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data} 
    return render(request, 'table.html', context) 
def aboutus(request):
    return render(request,'aboutus.html')