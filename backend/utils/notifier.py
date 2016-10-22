import requests

def notify(service, line):
    data = {'service': line.service.name,
            'source': line.source,
            'text': line.text}

    for notifier in service.notifier_set.all():
        sendNotification(notifier.url, data)


def sendNotification(url, data):
    requests.post(url, json=data)
