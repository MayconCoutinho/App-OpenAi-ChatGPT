from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Layout(BoxLayout):
    def load_text(self):
        pass
        # self.ids.label.text = "funcionando"
        
    def clear(self):
        pass
        # print("ta indo")
        # self.remove_widget(self.ids.label)
        
    def input_text(self):
        print("chegando: ", self.ids.txt.text)
        
        from gtts import gTTS
        from playsound import playsound
        import openai
        
        openai.api_key = "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"
        
        def ask_question(prompt):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens= 500,
                n=1,
                temperature=0.5,
            )

            answer = response.choices[0].text
            return answer
        
        user_input = self.ids.txt.text
        response = ask_question(user_input)
        tts = gTTS(response, lang='pt', tld='com.br', slow= False)
        print("Chatbot: ",response)
        tts.save('texto.mp3')    
        playsound('texto.mp3')

        

class App(App):
    def build(self):
        return Layout()
    
App().run()

# from kivy.app import App
# from kivy.uix.screenmanager import Screen, ScreenManager

# class TelaManager(ScreenManager):
#     pass 

# class Screen1(Screen):
#     def load_txt(self, txt):
#         print(txt)
#         self.ids.pesquisar_codigo.text=''


        

# class Screen2(Screen):
#     pass

# class App(App):
#     def build(self):
#         return TelaManager()
    
# App().run()


