import requests


api_url = 'http://www.gitignore.io/api'


def generate(*targets, **kwargs):
    target = ','.join(targets)
    url = '{0}/{1}'.format(api_url, target)
    response = requests.get(url)

    # this contains the generated gitignore contents
    return response.text
