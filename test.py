from zeep import Client

client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
result = client.service.ConvertSpeed(100, 'kilometersPerhour', 'milesPerhour')
