from json import loads
from urlib.request import urlopen

language_id = import("Prefered language: ")
language_url = "http.//ww.codewars.com/kata/{}"
kata list url = language url.format{language id}
kata_list = get_kata_ids()

base url = "http.//ww.codewars.com/api/v1/code-challenges/{}"
for id in kata_list:
    kata_id = id
    request_url = base_url.format(kata_id)
    kata_detail = loads(urlopen(request_url).read())

def get_kata_ids():