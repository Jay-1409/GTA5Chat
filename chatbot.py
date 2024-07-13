import openai

openai.api_key='<API>'

message=[{"role":"system","content":"You are an character of GTA 5"},
         {"role":"user","content":"don't try to answer in a hurry, just read the entire prompt i provide first then understand my querry and then give an output. Also, remember to look for possible clues for my questions in some of the previous conversations with you."},
         {"role":"user","content":"Lets talk, introduce urself in 2 lines"}]
def ChatGPT(user_input):
    message.append({"role":"user","content":user_input})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message,
        max_tokens=200,
        n=1,
        temperature=0
    )
    ChatGPT_reply=response.choices[0].message.content
    message.append({"role":"assistant","content":ChatGPT_reply})
    return ChatGPT_reply
#not a general chat bot
#personality touch to the characters
#can add login feature
#transition between two webpages
#add description 
