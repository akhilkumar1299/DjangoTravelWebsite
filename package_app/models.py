from django.db import models

# Create your models here.
class Theme(models.Model):
    name = models.TextField(blank=False)
    theme_img = models.ImageField(upload_to='images/')
    description = models.TextField()
    popular = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.name

class DomesticCategory(models.Model):
    name = models.TextField(blank=False,null=True)
    category_img = models.ImageField(upload_to='images/')
    popular = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.name

class InternationalCategory(models.Model):
    name = models.TextField(blank=False)
    category_img = models.ImageField(upload_to='images/')
    popular = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.name

class Package(models.Model):

    type_choice = (
        ('Domestic','Domestic'),
        ('International','International')
    )

    type = models.TextField(max_length=256,choices=type_choice, blank=False)
    pack_domestic_category = models.ManyToManyField(DomesticCategory, related_name='domestic_category', blank=True)
    pack_international_category = models.ManyToManyField(InternationalCategory, related_name='international_category')
    pack_theme_category = models.ManyToManyField(Theme, related_name='theme_category', blank=True)
    destination = models.CharField(max_length=256)
    dst_img = models.ImageField(upload_to='images/')
    vehicle = models.CharField(max_length=256,blank=True)
    tickets = models.CharField(max_length=256,blank=True)
    visa = models.BooleanField(null=False)
    note = models.TextField(blank=True)
    description = models.TextField(blank=True)
    offer = models.PositiveIntegerField(blank=True,null=True)
    popular = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.destination

class Hotel(models.Model):
    name = models.CharField(max_length=256)
    package = models.ManyToManyField(Package,related_name='hotels')
    url = models.URLField(unique=True)
    city = models.CharField(max_length=256)
    hotel_img = models.URLField(unique=True)
    star_rating = models.PositiveIntegerField(blank=True)
    display = models.BooleanField(null=False,default=False)

    def __str__(self):
        return self.name

class Inclusion(models.Model):
    name = models.CharField(max_length=256)
    package = models.ManyToManyField(Package,related_name='inclusions')

    def __str__(self):
        return self.name

class Exclusion(models.Model):
    name = models.CharField(max_length=256)
    package = models.ManyToManyField(Package,related_name='exclusions')

    def __str__(self):
        return self.name

class Faq(models.Model):
    query = models.CharField(max_length=256)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.query

# class About(models.Model):
#     company = models.CharField(max_length=256)
#     field1 = models.TextField(blank=True)
#     field2 = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.company

class Daywise(models.Model):

    duration_choice = (
            ('0 Night / 1 Day', '0 Night / 1 Day'),
            ('1 Night / 2 Days', '1 Night / 2 Days'),
            ('2 Nights / 3 Days', '2 Nights / 3 Days'),
            ('3 Nights / 4 Days', '3 Nights / 4 Days'),
            ('4 Nights / 5 Days', '4 Nights / 5 Days'),
            ('5 Nights / 6 Days', '5 Nights / 6 Days'),
            ('6 Nights / 7 Days', '6 Nights / 7 Days'),
            ('7 Night / 8 Days', '7 Night / 8 Days'),
            ('8 Nights / 9 Days', '8 Nights / 9 Days'),
            ('9 Nights / 10 Days', '9 Nights / 10 Days'),
            ('10 Nights / 11 Days', '10 Nights / 11 Days'),
            ('11 Nights / 12 Days', '11 Nights / 12 Days'),
            ('12 Nights / 13 Days', '12 Nights / 13 Days')
        )

    lowest = models.BooleanField(blank=False)
    package = models.ForeignKey(Package,related_name='daywiseschedules', on_delete=models.CASCADE)
    duration = models.CharField(max_length=256,choices=duration_choice)
    price_adult = models.PositiveIntegerField(blank=False)
    price_child = models.PositiveIntegerField(blank=True)
    price_infant = models.PositiveIntegerField(blank=True)

    day1_name = models.CharField(max_length=256,blank=True)
    day1 = models.TextField(blank=False)
    day2_name = models.CharField(max_length=256,blank=True)
    day2 = models.TextField(blank=True)
    day3_name = models.CharField(max_length=256,blank=True)
    day3 = models.TextField(blank=True)
    day4_name = models.CharField(max_length=256,blank=True)
    day4 = models.TextField(blank=True)
    day5_name = models.CharField(max_length=256,blank=True)
    day5 = models.TextField(blank=True)
    day6_name = models.CharField(max_length=256,blank=True)
    day6 = models.TextField(blank=True)
    day7_name = models.CharField(max_length=256,blank=True)
    day7 = models.TextField(blank=True)
    day8_name = models.CharField(max_length=256,blank=True)
    day8 = models.TextField(blank=True)
    day9_name = models.CharField(max_length=256,blank=True)
    day9 = models.TextField(blank=True)
    day10_name = models.CharField(max_length=256,blank=True)
    day10 = models.TextField(blank=True)
    day11_name = models.CharField(max_length=256,blank=True)
    day11 = models.TextField(blank=True)
    day12_name = models.CharField(max_length=256,blank=True)
    day12 = models.TextField(blank=True)
    day13_name = models.CharField(max_length=256,blank=True)
    day13 = models.TextField(blank=True)
    day14_name = models.CharField(max_length=256,blank=True)
    day14 = models.TextField(blank=True)
    day15_name = models.CharField(max_length=256,blank=True)
    day15 = models.TextField(blank=True)
    day16_name = models.CharField(max_length=256,blank=True)
    day16 = models.TextField(blank=True)
    day17_name = models.CharField(max_length=256,blank=True)
    day17 = models.TextField(blank=True)
    day18_name = models.CharField(max_length=256,blank=True)
    day18 = models.TextField(blank=True)
    day19_name = models.CharField(max_length=256,blank=True)
    day19 = models.TextField(blank=True)
    day20_name = models.CharField(max_length=256,blank=True)
    day20 = models.TextField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.package, self.duration)
