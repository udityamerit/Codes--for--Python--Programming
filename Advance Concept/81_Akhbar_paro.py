import requests
import json

my_api = "758213e1b2db4fbd82363f5cdb96d054"

def speak(str):
        from win32com.client import Dispatch
        speak = Dispatch("SAPI.spVoice")
        # speak.Speak("hello uditya how are you")
        speak.Speak(str)


if __name__== '__main__':
        speak("News for today")

        url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=758213e1b2db4fbd82363f5cdb96d054"

        news = requests.get(url).text
        news_dict = json.loads(news)
        # print(news_dict['articles'])
        arts = news_dict['articles']
        for article in arts:
                print(article['title'])
                print(f"if you want more details go to the given url===> {article['url']}/n")
                speak(article['title'])
                q = "If you want to read the content please press 1 if not press 0 "
                print(q)
                speak(q)
                
                inp = int(input())
                if(inp==1):
                        print(article['content'])

                        speak(article['content'])
                else:
                        continue
                speak("Moving on the next news..")
