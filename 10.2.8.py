from flask import Flask
import string

app = Flask(__name__)

def d_let():
    lst_keys = [i for i in range(1, len(string.ascii_uppercase)+1)] # for keys in letters
    lst_values= list(string.ascii_uppercase) #for value in letters
    letters = dict(zip(lst_keys, lst_values)) #{ 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", }
    return letters

@app.route('/get_letter/<int:index>')
def page_letter(index):
    letter = d_let().get(index)
    return letter

app.run()