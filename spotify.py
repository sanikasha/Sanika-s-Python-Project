import requests

url = "https://spotify23.p.rapidapi.com/search/"

querystring = {"q":"<REQUIRED>","type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}

headers = {
	"X-RapidAPI-Key": "45de2811f2mshc93a1328afeb302p1ee42bjsnbde76995c6f3",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

json = response.json() 

