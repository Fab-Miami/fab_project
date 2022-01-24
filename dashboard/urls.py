from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getbtc', views.get_btc, name='get_btc_ask'),
    path('popup-order-list', views.popup_order_list, name='popup_order_list'),




    path('chartjs/', views.chartjs, name='chartjs'),
    path('line-charts/', views.line_charts, name='line_charts'),
    path('bar-charts/', views.bar_charts, name='bar_charts'),
    path('candlestick-charts/', views.candlestick_charts, name='candlestick_charts'),
    path('geo-map/', views.geo_map, name='geo_map'),
    path('scatter-charts/', views.scatter_charts, name='scatter_charts'),
    path('pie-charts/', views.pie_charts, name='pie_charts'),
    path('radar-charts/', views.radar_charts, name='radar_charts'),
    path('heatmap-charts/', views.heatmap_charts, name='heatmap_charts'),


]