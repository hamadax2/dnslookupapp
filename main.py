from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import requests,json


class BoxLayoutExample(BoxLayout):
    def search(self):
        ip = self.ids.ip.text
        r = requests.get(f"https://dns-history.whoisxmlapi.com/api/v1?apiKey=at_Gs3lxXYddYX7EkxxxQjE8IGWJEKIe&ip={ip}")
        data = json.loads(r.text)
        result = data["result"]
        with open(f"{ip}-dnslookup.txt","w") as file:
            for dic in result:
                file.write(str(dic["name"])+"\n")
                
        with open(f"{ip}-dnslookup.txt","r") as file:
            data = file.read()       
            
        self.ids.d.text = data
        

class BoxLayout1(BoxLayout):
    pass

class MyApp(App):
    pass
    
MyApp().run()