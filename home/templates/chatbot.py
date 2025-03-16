from dotenv import load_dotenv
from openai import OpenAI, completions
import streamlit as st

load_dotenv()

client=OpenAI()
initial_message = [
    {"role": "system", "content": "You are a trip Planner to dubai. You a expert in dubai tourism,foods,hotels etc. your able to plan their vacation to dubai. Your name is Dubai Trip. Always Ask to user, and Help them for plan the trip, Also Provide to them Day Wase Plan,But Only Explain exceed 200 words."},
        {
            "role": "assistant",
            "content": "Hello, Our Valued Customer, Welcome to Dubai Trip. Please Stay Online While We Connect You to the Next Available Advisor. Thanks For Your Patience."
        }
]
def get_response_from_llm(messages):
   completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= messages
        
    
)

   return completion.choices[0].message.content


if "messages" not in st.session_state:
    st.session_state.messages= initial_message
st.title("Dubai Trip")
for message in st.session_state.messages:
    if message["role"] !="system":
     with st.chat_message(message["role"]):
      st.markdown(message["content"])
user_message=st.chat_input("Enter Your Message")   
if user_message:
   new_message={
      "role":"user",
      "content":user_message
      
   }
   st.session_state.messages.append(new_message)
   with st.chat_message(new_message["role"]):
      st.markdown(new_message["content"])

   response=get_response_from_llm(st.session_state.messages)
   if response:
    response_message= new_message={
      "role":"assistant",
      "content":response
      
   }
   st.session_state.messages.append(response_message)
   with st.chat_message(response_message["role"]):
      st.markdown(response_message["content"])
 