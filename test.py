import requests

BASE="http://127.0.0.1:5000/"

'''data=[{"likes":78, "name":"Joe", "views":100000},
	  {"likes":10000, "name":"How to make REST API", "views":80000},
	  {"likes":35, "name":"Ved", "views":2000}]

for i in range(len(data)):
	response=requests.put(BASE + "video/" + str(i), data[i])
	print(response.json())'''

response=requests.patch(BASE+"video/2", {"views":99, "likes":101})

#input()
#response=requests.get(BASE + "video/6")
print(response.json())