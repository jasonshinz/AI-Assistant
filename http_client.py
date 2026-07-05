import requests


class HttpClient:

    def get_json(self, url):

        response = requests.get(url)

        data = response.json()

        response.close()

        return data