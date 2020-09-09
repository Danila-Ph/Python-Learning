import requests
url = 'http://tutmed.by/cgi-bin/is11_60?sfl_=317'
r = requests.get(url)
print(r.encoding)
with open('test.html', 'wb') as output_file:
  output_file.write(r.text.encode("KOI8-r"))
