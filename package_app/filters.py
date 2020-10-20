from package_app.models import Package
import django_filters

class PackageFilter(django_filters.FilterSet):
    destination = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Package
        fields = ['destination',]
