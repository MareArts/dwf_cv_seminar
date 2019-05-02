dic_a = {}

dic_a['name'] = 'leon'
dic_a['score'] = [1, 2, 3, 4]
print(dic_a)


list_b = []
list_b.append( {'name':'elin', 'score':[5, 6, 7, 8]} )
list_b.append( dic_a )
print(list_b)



#dic to json
import json
str_type = json.dumps(list_b, indent=10) #dic to json
#write json to file
f= open("./day2/json.json","w+")
f.write(str_type)
f.close

