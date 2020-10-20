from django.conf.urls import url
from package_app import views
from .filters import PackageFilter
from django_filters.views import FilterView

app_name = 'package_app'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>\d+)/$',views.PackageDetailView.as_view(),name='detail'),
    url(r'^domestic/',views.DomesticListView.as_view(),name='domestic'),
    url(r'^international/',views.InternationalListView.as_view(),name='international'),
    url(r'^india_category/(?P<pk>\d+)/$',views.DomesticCategoryDetailView.as_view(),name='domestic_category_detail'),
    url(r'^international_category/(?P<pk>\d+)/$',views.InternationalCategoryDetailView.as_view(),name='international_category_detail'),
    url(r'^theme_category/(?P<pk>\d+)/$',views.ThemeCategoryDetailView.as_view(),name='theme_category_detail'),
    url(r'^pdf_view/(?P<pk>\d+)/$',views.GeneratePdf.as_view(),name='generate_pdf'),
    url(r'^search_result/$', FilterView.as_view(filterset_class=PackageFilter, template_name='package_app/search_result.html'), name='search_result'),
]
