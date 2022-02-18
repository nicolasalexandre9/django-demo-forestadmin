from datetime import date, time

from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200).unique
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    label = models.CharField(max_length=200)
    price = models.DecimalField
    token = models.UUIDField(null=True)
    delivery_date = models.DateField(default=date.today(), null=True)
    delivery_hour = models.TimeField(default=time(), null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    label = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Range(models.Model):
    label = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    DifficultyChoices = models.TextChoices('DifficultyChoices', 'easy hard')
    label = models.CharField(max_length=200)
    comment = models.TextField()
    difficulty = models.CharField(blank=True, choices=DifficultyChoices.choices, max_length=10)
    amount = models.FloatField()
    active = models.BooleanField(default=True)
    options = models.JSONField
    other = models.CharField(max_length=200, default='N/A')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    ranges = models.ManyToManyField(Range)


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


class Bookstore(models.Model):
    label = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)


class Author(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


class Editor(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
