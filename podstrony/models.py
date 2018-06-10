from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Budowa(models.Model): 
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='budowa_image', blank=True)

    def __str__(self):
        return self.headline

class Teoria(models.Model): 
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='teoria_image', blank=True)

    def __str__(self):
        return self.headline


class Przepisy(models.Model): 
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class Meteorologia(models.Model): 
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class Image(models.Model): 
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    article = models.CharField(max_length=200)
    img = models.ImageField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline

