import openai
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext
import threading

# Set up your OpenAI API key
openai.api_key = "sk-GaGWkyTUvZRwoFlSecDVDsWK8jWqf40kKDCV7zpstPT3BlbkFJi1Mk1piJzVMcD16Bps_xLp7NjBo-REFBI91jRKs1kA"

class VoiceChatbot:
    def __init__(self, master):
        self.master = master
        master.title("AI Voice Chatbot")
        master.geometry("600x400")
        master.configure(bg="#F0F8FF")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=70, height=20, bg="#FFFFFF")
        self.chat_history.pack(padx=10, pady=10)

        self.input_field = tk.Entry(master, width=50)
        self.input_field.pack(side=tk.LEFT, padx=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message, bg="#4CAF50", fg="white")
        self.send_button.pack(side=tk.LEFT, padx=5)

        self.voice_button = tk.Button(master, text="🎤 Voice", command=self.toggle_voice_input, bg="#008CBA", fg="white")
        self.voice_button.pack(side=tk.LEFT, padx=5)

        self.is_listening = False
        self.setup_voice()

    def setup_voice(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def send_message(self):
        user_input = self.input_field.get()
        if user_input:
            self.chat_history.insert(tk.END, f"You: {user_input}\n")
            self.input_field.delete(0, tk.END)
            self.get_ai_response(user_input)

    def get_ai_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=f"Human: {user_input}\nAI:",
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            ai_response = response.choices[0].text.strip()
            self.chat_history.insert(tk.END, f"AI: {ai_response}\n")
            self.chat_history.see(tk.END)
            self.speak(ai_response)
        except Exception as e:
            print(f"Error in getting AI response: {e}")
            self.chat_history.insert(tk.END, "AI: Sorry, I encountered an error. Please try again.\n")

    def toggle_voice_input(self):
        if not self.is_listening:
            self.is_listening = True
            self.voice_button.config(bg="#FF4500")
            threading.Thread(target=self.listen_for_speech).start()
        else:
            self.is_listening = False
            self.voice_button.config(bg="#008CBA")

    def listen_for_speech(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.is_listening:
                try:
                    audio = self.recognizer.listen(source, timeout=5)
                    user_input = self.recognizer.recognize_google(audio)
                    self.master.after(0, self.process_voice_input, user_input)
                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                except Exception as e:
                    print(f"Error in speech recognition: {e}")

    def process_voice_input(self, user_input):
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, user_input)
        self.send_message()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceChatbot(root)
    root.mainloop()