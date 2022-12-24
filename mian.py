import requests

# I use a Free api to change text to morse code, but you can just send 5 request per hour
# maybe later I must build a free api to this for other student
API_URL = "https://api.funtranslations.com/translate/morse.json"
dot = "⚫"
line = "━━━"
output = ""
print("Input a word We Change it to morse code for you")
user_input = input("Enter a word and Press Enter")
headers = {
    "text": user_input
}
response = requests.get(API_URL, params=headers)
data = response.json()

for txt in data["contents"]["translated"]:
    output += " "
    if txt == ".":
        output += dot
    elif txt == "-":
        output += line
    else:
        output += txt

print(output)

