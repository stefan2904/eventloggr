from django.db import models


class Service(models.Model):
    """Service which reports loglines to us.
    """
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.name.encode('ascii', errors='replace'))


class Endpoint(models.Model):
    """Endpoint to which a service script can report loglines.
    One service can have multiple endpoints.
    """
    service = models.ForeignKey('Service')
    url = models.CharField(max_length=255, null=False, blank=False)
    secret = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return '{} ({})'.format(self.service, self.url)


class Logline(models.Model):
    """A logline of a service.
    """
    date = models.DateTimeField(auto_now=True)
    identifier = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False)
    service = models.ForeignKey('Service', null=False, blank=False)
    source = models.CharField(max_length=255, null=False, blank=False)
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        source = self.source.encode('ascii', errors='replace')
        service = self.service
        text = self.text.encode('ascii', errors='replace')
        return '[{}] {}: {} '.format(service, source, text)


class Notifier(models.Model):
    """External services to notify every time a new logline arrives for a service.
    One notifier can be attached to multiple services.
    A Service can have multiple notifier.
    """
    service = models.ManyToManyField(Service)
    url = models.CharField(max_length=255, null=False, blank=False)
    secret = models.CharField(max_length=255, null=False, blank=False)
    last = models.IntegerField(default=-1)

    def __str__(self):
        return 'to {}'.format(self.url)
