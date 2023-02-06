from django.db import models

class Province(models.Model):
    name = models.CharField(max_length = 10)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name 

class City(models.Model):
    name = models.CharField(max_length = 5)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name 

class Person(models.Model):
    firstname = models.CharField(max_length = 10)
    lastname = models.CharField(max_length = 10)
    visitation = models.ManyToManyField(City, related_name = "visitor")
    hometown = models.ForeignKey(City, related_name = "birth",on_delete=models.CASCADE)
    living = models.ForeignKey(City, related_name = "citizen",on_delete=models.CASCADE)
    def __unicode__(self):
        return self.firstname + self.lastname
    def __str__(self):
        return self.firstname 



class Publisher(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300, default='Lahore', null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'books'

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    class Meta:
        default_related_name = 'stores'

    def __str__(self):
        return self.name
