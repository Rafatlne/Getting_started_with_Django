import datetime
from django.db import models

class User(models.Model):
    first_name = models.CharField("person's first name", max_length = 30)
    last_name = models.CharField("person's last name", max_length = 30)
    cars = models.ManyToManyField('Car', verbose_name="the user's cars")

STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
)

class Website(models.Model):
    name = models.CharField(max_length = 50)
    url = models.URLField()
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def was_released_last_week(self):
        if self.release_date < datetime.date(2019, 3, 3):
            return "Released before last week"
        return "Released this week"

    @property
    def get_full_name(self):
        return f"This is my website's full name: {self.name}"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"website/{self.id}"

    def save(self, *args, **kwargs):
        print("we are doing something else here...")
        super().save(*args, **kwargs)
    # class Meta:
    #     ordering="rating"
    #     db_table="website_custome_table_name"
    #     verbose_name="the website"
    #     verbsose_name_plural="the websites"

class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
