from gtts import gTTS
from playsound import playsound
import openai

openai.api_key = "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"


def ask_question(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens= 300,
        n=1,
        temperature=0.5,
    )

    answer = response.choices[0].text
    return answer

while True:
    user_input = input("Você: ")
    response = ask_question(user_input)
    tts = gTTS(response, lang='pt', tld='com.br', slow= False)
    print("Chatbot: ",response)

    tts.save('texto.mp3')
    playsound('texto.mp3')





