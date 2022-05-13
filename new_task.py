from flask import Flask, request, render_template

app = Flask(__name__)
# У вас если словарик, где ключи - это int
#
d_city = {1: "Самара", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород"}
#
# Напишите вьюшку  /city/<число>, которая будет возвращать
# название города по его номеру в словаре

@app.route('/')
def page_index():
    return "It works"

@app.route('/city/<int:sid>')
def city(sid):
    return d_city.get(sid)

app.run(debug=True)