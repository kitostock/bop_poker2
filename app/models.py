from django.db import models

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title


class Task(models.Model):

    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title


class BopInfo(models.Model):
    user_id = models.CharField(max_length=11)
    category_id = models.CharField(max_length=11)
    rate_id = models.CharField(max_length=11)
    buy_in = models.IntegerField(max_length=255)
    cash_out = models.IntegerField(max_length=255)
    number_of_hands = models.IntegerField(max_length=255)
    register_date = models.DateTimeField(blank=True, null=True)
    memo = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class PersonalCategory(models.Model):
    category_id = models.CharField(max_length=11, primary_key=True)
    user_id = models.CharField(max_length=11)
    category_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.category_id) + " - " + self.category_name

class PersonalRate(models.Model):
    rate_id = models.CharField(max_length=11, primary_key=True)
    user_id = models.CharField(max_length=11)
    rate_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.rate_id) + " - " + self.rate_name
