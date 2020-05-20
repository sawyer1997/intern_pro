from django.db import models


# Create your models here.
class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=20)
    referral_count = models.IntegerField(default=1)
    is_referenced = models.BooleanField(default=False)
    referred_id = models.IntegerField(null=True)
    created_on = models.DateTimeField('Created_on', auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def update_referral_count(self):
        self.referral_count += 1
        self.save()

    def update_referred_id(self, id):
        self.is_referenced = True
        self.referred_id = id
        self.save()
