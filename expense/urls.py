from django.conf.urls import patterns, include, url
from tracker.views import InvoiceListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expense.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^invoices/$', InvoiceListView.as_view()),
)
