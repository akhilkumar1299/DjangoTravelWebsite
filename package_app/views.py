from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from package_app.models import Package,DomesticCategory, InternationalCategory, Faq, Theme
from . import models
from django_xhtml2pdf.views import PdfMixin

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['Package'] = Package.objects.all()
        context['Domestic'] = DomesticCategory.objects.all()
        context['International'] = InternationalCategory.objects.all()
        context['Theme'] = Theme.objects.all()
        context['Faq'] = Faq.objects.all()
        return context

class DomesticListView(ListView):
    context_object_name = 'domestic_list'
    model = models.Package
    template_name = 'package_app/package_domestic.html'

class InternationalListView(ListView):
    context_object_name = 'international_list'
    model = models.Package
    template_name = 'package_app/package_international.html'

class PackageDetailView(DetailView):
    context_object_name = 'package_detail'
    model = models.Package
    template_name = 'package_app/package_detail.html'

class AboutView(TemplateView):
    template_name = 'aboutus.html'

class DomesticCategoryDetailView(DetailView):
    model = models.DomesticCategory
    context_object_name = 'domestic_detail'
    template_name = 'package_app/domestic_category.html'

class InternationalCategoryDetailView(DetailView):
    model = models.InternationalCategory
    context_object_name = 'international_detail'
    template_name = 'package_app/international_category.html'

class ThemeCategoryDetailView(DetailView):
    model = models.Theme
    context_object_name = 'theme_detail'
    template_name = 'package_app/theme_category.html'

class GeneratePdf(PdfMixin, DetailView):
    model = models.Package
    template_name = "package_app/pdf_template.html"
    context_object_name = 'package_detail_pdf'
