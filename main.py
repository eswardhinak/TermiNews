import urllib.request
import json 
import sys


def main():
	num_articles = 0	#number of articles to display
	#default number of articles
	if (len(sys.argv) < 2):
		num_articles = 5

	#try to convert first argument to number of articles
	try: 
		num_articles = int(sys.argv[1])
	#if it isn't catch the exception
	except ValueError:
		print("Not a valid argument:", sys.argv[1])
		return

	#if we have a wrong argument
	if num_articles not in range(1,21):
		print("Incorrect value:", num_articles)
		print("Number of articles must be between 1 and 20.")
		return

	response="foo"
	url= constructURL()

	try: 
		response = urllib.request.urlopen(url)			
		if response.getcode() == 200:
			pass
		else:
			print (response.getcode())
	except Exception as inst:
		print (inst)
		return
	read_response = response.read()
	str_response = read_response.decode(encoding="utf-8")
	json_data = json.loads(str_response)
	count = 0
	print("----------------------------------------")
	for i in json_data["results"]:
		if count == num_articles:
			break
		print(i["title"])
		print ("\t" + i["abstract"])
		print(i["url"])
		print("----------------------------------------")
		count += 1

def constructURL():
	base_url = 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/1.json?api-key='
	f = open("keys.json")
	json_data = json.load(f)
	key = json_data["Most Popular"]
	url = base_url + key
	return url

if __name__ == "__main__": main()
