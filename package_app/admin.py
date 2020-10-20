from django.contrib import admin
from package_app.models import Package, Hotel, Inclusion, Exclusion, Faq, Daywise, Theme, DomesticCategory, InternationalCategory
# Register your models here.
admin.site.register(Package)
admin.site.register(Hotel)
admin.site.register(Inclusion)
admin.site.register(Exclusion)
admin.site.register(Faq)
admin.site.register(Daywise)
admin.site.register(Theme)
admin.site.register(DomesticCategory)
admin.site.register(InternationalCategory)
# admin.site.register(About)
# admin.site.register(Feedback)
