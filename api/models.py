from django.db import models


class Feedback(models.Model):
    full_name = models.CharField(max_length=111)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name

class Dashboard(models.Model):
    name = models.ForeignKey('Region', on_delete=models.CASCADE)
    number_of_donors = models.IntegerField()
    planted_trees = models.IntegerField()
    being_planted_tree = models.IntegerField()

    def __str__(self):
        return str(self.name)


class TreePrice(models.Model):
    tree_name = models.ForeignKey('TreeName', on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return '{} = {}'.format(self.tree_name, self.price)

class TreeType(models.Model):

    name = models.CharField(max_length=111)

    def __str__(self):
        return self.name

class TreeName(models.Model):

    name = models.CharField(max_length=111)
    tree_type = models.ForeignKey('TreeType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=111)

    def __str__(self):
        return self.name

class District(models.Model):

    name = models.CharField(max_length=111)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tree(models.Model):
    tree_type = models.ForeignKey('TreeType', on_delete=models.CASCADE)
    tree_name = models.ForeignKey('TreeName', on_delete=models.CASCADE)
    tree_number = models.IntegerField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.tree_name, self.tree_type, self.tree_number)

class Client(models.Model):
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    district = models.ForeignKey('District', on_delete=models.CASCADE)
    neighborhood_by = models.BooleanField(default=False)
    neighborhood = models.CharField(max_length=111, blank=True)
    url = models.URLField()

    def __str__(self):
        return "{} {}".format(self.region, self.district)

