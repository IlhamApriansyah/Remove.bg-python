import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file' : open ('Background.jpg', 'rb')},
    data={'semitransparency' : 'true'},
    headers={'X-Api-Key' : 'jo7sfS2p15iePwT3ugGDzK2D'},
)

if response.status_code == requests.codes.ok:
    print("sukses!!")
    with open('remove-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error banh, karena :", response.status_code, response.text)
