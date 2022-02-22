from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .api import *
import datetime


def index(request):
    quote = CoinbaseApi()
    context = {'btc_ask' : quote.get_bitcoin_quote()['ask'], 'btc_bid' : quote.get_bitcoin_quote()['bid'], 'onehundred' : range(100)}
    return render(request, 'dashboard/index.html', context)


def get_btc(request):
    quote = CoinbaseApi()
    btc_ask = '{0:.2f}'.format(float(quote.get_bitcoin_quote()['ask']))
    btc_bid = '{0:.2f}'.format(float(quote.get_bitcoin_quote()['bid']))
    context = {'btc_ask' : btc_ask, 'btc_bid' : btc_bid, 'onehundred' : range(100)}
    return render(request, 'dashboard/widgets/info-bar.html', context)

def popup_order_list(request):
    context = {'onehundred' : range(100)}
    return render(request, 'dashboard/widgets/popup-order-list.html', context)










def chartjs(request):
    stuff = 'blabla'
    context = {'bla': stuff}
    return render(request, 'dashboard/charts/chartjs.html', context)

def line_charts(request):
    stuff = 'blabla'
    context = {'bla': stuff}
    return render(request, 'dashboard/charts/line-charts.html', context)

def bar_charts(request):
    stuff = 'blabla'
    context = {'bla': stuff}
    return render(request, 'dashboard/charts/bar-charts.html', context)

def candlestick_charts(request):
    stuff = 'blabla'
    context = {'bla': stuff}
    return render(request, 'dashboard/charts/candlestick-charts.html', context)

def geo_map(request):
    stuff = 'blabla'
    context = {'bla': stuff}
    return render(request, 'dashboard/charts/geo-map.html', context)

def scatter_charts(request):
    stuff = 'blabla'
    context = {'bla': stuff}
    return render(request, 'dashboard/charts/scatter-charts.html', context)

def pie_charts(request):
    stuff = 'blabla'
    context = {'bla': stuff}
    return render(request, 'dashboard/charts/pie-charts.html', context)

def radar_charts(request):
    stuff = 'blabla'
    context = {'bla': stuff}
    return render(request, 'dashboard/charts/radar-charts.html', context)

def heatmap_charts(request):
    stuff = 'blabla'
    context = {'bla': stuff}
    return render(request, 'dashboard/charts/heatmap-charts.html', context)