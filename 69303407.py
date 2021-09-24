from urllib import parse

url = 'https://www.exmple.com/test?test1=abc&test2=abc&test3=abc&q=/"TEST"/"TEST"'
encoded = parse.quote_plus(url.split("&q=")[1])
encoded_url = f"{url.split('&q=')[0]}&q={encoded}"
print(encoded_url)
print('https://www.exmple.com/test?test1=abc&test2=abc&test3=abc&q=%2F%22TEST%22%2F%22TEST%22%20')
