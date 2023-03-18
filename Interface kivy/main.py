from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Layout(BoxLayout):
    def voice_identify(self):
        from gtts import gTTS
        from playsound import playsound
        from os import remove
        import speech_recognition as sr
        import openai

        def text_voz(txt):
            """
            Função para transformar texto em voz.
            """
            
            try:
                tts = gTTS(text=txt, lang='pt', tld='com.br', slow=False)
                tts.save('texto.mp3')
                playsound('texto.mp3')
                remove('texto.mp3')
            except Exception as e:
                print(f"Alguma coisa deu errado no text_voz: {e}")
        
        def input_voz():
            """
            Função para reconhecimento de voz do usuário.
            """
            rec = sr.Recognizer()
            with sr.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic)
                text_voz("Pergunte-me algo.")
                audio = rec.listen(mic)
            try:
                texto = rec.recognize_google(audio, language="pt-BR")
                print("Você disse:", texto)
                return texto
            except sr.UnknownValueError:
                text_voz("Não entendi. Tente novamente.")

        def ask_question(prompt):
            """
            Função para enviar a pergunta do usuário para a API da OpenAI e obter a resposta.
            """
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=300,
                n=1,
                temperature=0.5,
            )

            answer = response.choices[0].text.strip()
            return answer

        
        user_input = input_voz()
        response = ask_question(user_input)
        text_voz(response)

class App(App):
    def build(self):
        return Layout()
    
App().run()


