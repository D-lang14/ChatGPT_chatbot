import openai
import config
import pyttsx3

api_key = config.DevelopmentConfig.OPENAI_KEY
openai.api_key = api_key

def voice(answer):
    sound = pyttsx3.init()
    sound.say(answer)
    sound.runAndWait()

def generateChatResponse(prompt):
    message = []
    message.append(
        {"role": "system", "content": "You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    message.append(question)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=message)
    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
        
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists, come back later.'
    
    voice(answer)
    return answer


