from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def elements(self):
        return list(self.menu_elements.values_list('name', 'url'))


class MenuElement(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_elements')
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128, default='/')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=256,)
    date_release = models.DateField(blank=True)
    description = models.TextField(max_length=1024, blank=True)
    poster = models.ImageField(upload_to='film/poster/')
    trailer_url = models.URLField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date_release',)


class News(models.Model):
    name = models.CharField(max_length=256,)
    description = models.TextField(max_length=5024, blank=True)
    image = models.ImageField(upload_to='film/poster/')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
