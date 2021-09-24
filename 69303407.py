from urllib import parse

url = 'https://www.exmple.com/test?test1=abc&test2=abc&test3=abc&q=/"TEST"/"TEST"&test3=abc&test4=jksdfh'
encoded = parse.quote_plus(url.split("&q=")[1])
encoded_url = f"{url.split('&q=')[0]}&q={encoded}"
print(encoded_url)
print('https://www.exmple.com/test?test1=abc&test2=abc&test3=abc&q=%2F%22TEST%22%2F%22TEST%22%20')


url = 'https://www.exmple.com/test?test1=abc&test2=abc&test3=abc&q=/"TEST"/"TEST"&utm_source=test1&cpc=123&gclid=abc123'
# the first parameter is always delimited by a ?
baseurl, parameters = url.split("?")
newparameters = []
for parameter in parameters.split("&"):
    # check if the parameter is the part that needs to be encoded
    if parameter.startswith("q="):
        # encode the parameter
        print(parameter[2:])
        newparameters.append(f"q={parse.quote_plus(parameter[2:])}")
    else:
        # otherwise add the parameter unencoded
        newparameters.append(parameter)
# string magic to create the encoded url
encoded_url = f"{baseurl}?{'&'.join(newparameters)}"
print(encoded_url)