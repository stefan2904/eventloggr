from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.name)


class Endpoint(models.Model):
    service = models.ForeignKey('Service')
    url = models.CharField(max_length=255, null=False, blank=False)
    secret = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return '{} ({})'.format(self.service, self.url)


class Logline(models.Model):
    date = models.DateTimeField(auto_now=True)
    identifier = models.CharField(max_length=255, unique=True, null=False, blank=False)
    service = models.ForeignKey('Service', null=False, blank=False)
    source = models.CharField(max_length=255, null=False, blank=False)
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        return '{}@{}:  {}'.format(self.source, self.service, self.text)


class Notifier(models.Model):
    service = models.ManyToManyField(Service)
    url = models.CharField(max_length=255, null=False, blank=False)
    secret = models.CharField(max_length=255, null=False, blank=False)
    last = models.IntegerField(default=-1)

    def __str__(self):
        return 'to {}'.format(self.url)
