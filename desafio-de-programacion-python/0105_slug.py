import re
def sligfy(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9 ]','', text)
    text = text.replace(' ', '-')
    return text

print(sligfy('no-se que eL est!o'))