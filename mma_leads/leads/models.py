from django.db import models

class Stage(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    is_final = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Request(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    channel = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lead(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='leads')
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True, related_name='leads')

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    channel = models.CharField(max_length=50)

    client_type = models.CharField(max_length=50, default='adult')
    sport = models.CharField(max_length=50, blank=True)
    trainer = models.CharField(max_length=50, blank=True)

    pre_trial_status = models.CharField(max_length=50, default='none')
    trial_status = models.CharField(max_length=50, default='none')
    result = models.CharField(max_length=50, default='none')

    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=10, default='KGS')
    comment = models.TextField(blank=True)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
