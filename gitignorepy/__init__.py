import requests


api_url = 'http://www.gitignore.io/api'


def generate(*targets, **kwargs):
    """
    Requests gitignore.io and returns the generated gitignore contents
    @param targets      the languages/frameworks that the generated
                        gitignore is for
    @return string      the generated gitignore contents
    """
    target = ','.join(targets)
    url = '{0}/{1}'.format(api_url, target)
    response = requests.get(url)

    # this contains the generated gitignore contents
    return response.text
