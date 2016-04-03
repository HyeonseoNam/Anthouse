from django.conf.urls import url, patterns
from sdata.views import StockListView


urlpatterns = patterns('sdata.views',
    # url(r'^$', 'index', name='index'),
    # url(r'^(?P<pk>\d+)/$', 'data_test', name='data_test'),
    url(r'^$', 'data_test', name='data_test'),
    url(r'^api/stock/$', 'stock_data', name='stock_data'),
    # url(r'^2$', 'data_test', name='data_test'),
    # url(r'^$', StockListView.as_view(), name='data_test'),





    )


# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
