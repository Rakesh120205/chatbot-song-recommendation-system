import re
import random

response = {
    "hello":["Hello, how can I help you."],
    
    "Introduce yourself": ["I'm a chatbot designed to assist you. My goal is to provide helpful information and answer your questions"],
    
    "how are you": ["I am fine, what about you?"],
    
    "I'm feeling really happy today!": ["That's wonderful to hear! What's making you so happy? Anything specific you'd like to share or talk about?"],
    
    "Feeling a bit sad right now.": ["I'm sorry to hear that. It's okay to feel down sometimes. Is there anything specific on your mind, or would you like to talk about what's bothering you?"],
    
    "I'm so stressed with work right now.": ["I understand that work stress can be overwhelming. What aspects of work are causing stress, and is there anything I can do to help or provide some relaxation tips?"],
    
    "I got some exciting news today!": ["That's fantastic! Congratulations! I'd love to hear more about your exciting news. What happened?"],
    
    "Feeling anxious about an upcoming event.": [ "It's normal to feel anxious before important events. What specifically is causing you anxiety? If you'd like, we can talk through it together."],
    
    "Just a regular day, nothing special.": ["That's okay! Sometimes, regular days are just what we need. Anything on your mind, or would you like to chat about something specific?"],
     
    "I'm curious about learning something new.": ["That's great! Curiosity is a wonderful trait. What topic are you interested in, or is there a specific question you'd like me to help you explore?"],
    
    "Feeling bored right now.": [ "Boredom happens to the best of us. Is there a particular activity or topic you'd like to engage in to make things more interesting?"],
    
    "i feel (.*)": ["How long have you been feeling {}?"],

    "i am (.*)": ["How long have you been {}?"],

    "i'm (.*)":["Why are you {}?", "How long have you been {}?"],

    "analyze my mood": ["https://open.spotify.com/playlist/0RH319xCjeU8VyTSqCF6M4"],

    "recommend me (.*) songs":["https://open.spotify.com/playlist/37i9dQZF1DX3SQwW1JbaFt"],

    "i (.*) you":["Why do you {} me?", "What makes you think you {} me?"],

    "i (.*) myself": ["Why do you {} yourself?", "What makes you think you {} yourself?"],

    "(.*) sorry (.*)":["There's no need to apologize.", "What are you apologizing for?"],

    "(.*) friend (.*)": ["Tell me more about your friend.", "How do your friends make you feel?"],

    "yes":["You seem quite sure.", "Ok, but can you elaborate."],

    "no":["Why not?", "Ok, but can you elaborate a bit?"],

    " (.*) ":["Please tell me more.", "let's change focus a bit... tell me about your family."],

    "":["Why do you think that?"],


}


def match_response(input_text):
  #Create a for loop to iterate over the items of the "response" dictionary.
  for pattern, response_list in response.items():
    matches = re.match(pattern, input_text.lower())
    if matches:
      chosen_response = random.choice(response_list)
      return chosen_response.format(*matches.groups())
  return "I'm sorry I don't understand what you're saying."

print("Welcome to the Chatbot Song Recommendation System")
while True:
  user_input = input("You: ")
  if user_input.lower() == "bye":
    print("Chatbot: Goodbye.")
    break
  else:
    print("Chatbot: "+match_response(user_input))
