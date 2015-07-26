import urllib.request
import json 

def main():

#url = 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=4fd3f6a9801451c2a0111bccb516d28a%3A16%3A72566955'
	response="foo"
	url= constructURL()
	while True:
		try: 
			response = urllib.request.urlopen(url)
			if response.getcode() == 200:
				break
			else:
				print (response.getcode())
		except Exception as inst:
			print (inst)
	read_response = response.read()
	str_response = read_response.decode(encoding="utf-8")
	json_data = json.loads(str_response)

	for i in json_data["results"]:
		print (i["title"])
		print ("\t" + i["abstract"])

def constructURL():
	base_url = 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key='
	f = open("keys.json")
	json_data = json.load(f)
	key = json_data["Most Popular"]
	url = base_url + key
	return url

if __name__ == "__main__": main()
