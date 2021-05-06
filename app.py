from flask import Flask, request, render_template
from words import koverk  
  

app = Flask(__name__)    
  
intro = """
Автоматический коверкатель слов версии 0.3. Для того, чтобы исковеркать
слово, необходимо ввести его в поле справа и нажать кнопку "исковеркать". Введенные и исковерканные
слова будут отображаться в словаре справа. Словарь вмещает в себя 25 свежих исковерканных слов. 
"""

class Word:
    def __init__(self, word):
        self.word = word
    
    def koverking(self):
        return koverk(self.word)


dictionary = {}

@app.route('/', methods =["GET", "POST"]) 
def koverked(): 
    if request.method == "POST": 
        word = Word(request.form.get("word"))
        word.word = word.word.lower()
        if word not in dictionary.keys():
           dictionary[word.word] = word.koverking()
        if len(dictionary) >= 26:
            del dictionary[next(iter(dictionary))]
        return render_template("form.html", coverked_word=word.koverking(), dict=dictionary, intro=intro) 
    return render_template("form.html", coverked_word='', dict=dictionary, intro=intro) 
  
if __name__=='__main__': 
   app.run() 