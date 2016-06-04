''' Credit goes to Adam Eubanks for teaching me this
where it says Your APP ID Here, go create a wolframalpha user id
Then create a new app and copy your unique APP id into the quotations
'''

import wolframalpha

input = raw_input("Question: ")
app_id = "Your APP ID Here"
client = wolframalpha.Client(app_id)
	
res = client.query(input)
answer = next(res.results).text

print(answer)
