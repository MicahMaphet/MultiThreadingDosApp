def makeValid(text):
    remText = text
    deleteTo = -1
    text = text.lower().strip()
    if text.find('https://') == -1:
        text = 'https://' + text
    elif text.find('https://') > 0:
        deleteTo = text.find('https://')
        remText = text
        text = ''
        # Deletes up to https://
        for i in range(len(remText)):
            if i >= deleteTo:
                text = text + remText[i]
    print(text)
    return text

print(makeValid("    agvygvgvvhugvhttpsugvhttps://GoOgle.com    "))

def valid(url):
    if url.find('https://') == 0 and url.find('.') > 8 and len(url) > 9:
        return True
    return False

