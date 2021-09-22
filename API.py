import requests
import json
url="http://saral.navgurukul.org/api/courses"
a=requests.get(url).text
dic=json.loads(a)
a=1
list_id=[]
for i in dic["availableCourses"]:
    print(a,i["name"])
    list_id.append(i["id"])
    a+=1
user_input=int(input("enter your course number what you read:-"))
course_id=list_id[user_input-1]
b=requests.get("https://saral.navgurukul.org/api/courses/"+course_id+"/exercises").text
dic2=json.loads(b)
print(type(dic2))
num=1
slug_list=[]
for j in dic2["data"]:
    print(num,j["name"])
    slug_list.append(j["slug"])
    for k in j["childExercises"]:
        num+=1
        print("  ",num,k["name"])
        slug_list.append(k["slug"])
    num+=1
user_input2=int(input("select your what ever you want to read:-"))
slug_id=slug_list[user_input2-1]
dic3=requests.get(" http://saral.navgurukul.org/api/courses/"+course_id+"/exercise/getBySlug?slug="+slug_id).text
d=json.loads(dic3)
c=d["content"]
e=json.loads(c)
for l in e:
    final_data=l["value"].strip()
    print(final_data)