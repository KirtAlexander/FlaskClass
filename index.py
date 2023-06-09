from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)
allProducts = [
    {
        "id": 1,
        "nombre": "Laptop",
        "cantidad": 10,
        "precio": 1500
    },
    {
        "id": 2,
        "nombre": "Teléfono inteligente",
        "cantidad": 20,
        "precio": 800
    },
     {
        "id": 3,
        "nombre": "Smart TV",
        "cantidad": 5,
        "precio": 1200
    },
     {
        "id": 4,
        "nombre": "Cámara digital",
        "cantidad": 15,
        "precio": 500
    },
     {
        "id": 5,
        "nombre": "Tablet",
        "cantidad": 8,
        "precio": 300
    },
     {
        "id": 6,
        "nombre": "Auriculares inalámbricos",
        "cantidad": 25,
        "precio": 150
    },
     {
        "id": 7,
        "nombre": "Monitor",
        "cantidad": 12,
        "precio": 400
    },
     {
        "id": 8,
        "nombre": "Impresora",
        "cantidad": 7,
        "precio": 200
    },
     {
        "id": 9,
        "nombre": "Altavoz Bluetooth",
        "cantidad": 18,
        "precio": 100
    },
    {
        "id": 10,
        "nombre": "Router Wi-Fi",
        "cantidad": 6,
        "precio": 80
    },
    {
        "id": 11,
        "nombre": "Smartwatch",
        "cantidad": 14,
        "precio": 250
    },
     {
        "id": 12,
        "nombre": "Consola de videojuegos",
        "cantidad": 3,
        "precio": 450
    },
     {
        "id": 13,
        "nombre": "Teclado mecánico",
        "cantidad": 9,
        "precio": 120
    },
     {
        "id": 14,
        "nombre": "Mouse inalámbrico",
        "cantidad": 22,
        "precio": 50
    },
  {
        "id": 15,
        "nombre": "Disco duro externo",
        "cantidad": 11,
        "precio": 100
    },
    {
        "id": 16,
        "nombre": "Bocina inteligente",
        "cantidad": 16,
        "precio": 180
    },
    {
        "id": 17,
        "nombre": "Cargador portátil",
        "cantidad": 20,
        "precio": 30
    },
 {
        "id": 18,
        "nombre": "Tarjeta de memoria",
        "cantidad": 30,
        "precio": 25
    },
     {
        "id": 19,
        "nombre": "Monitor gaming",
        "cantidad": 8,
        "precio": 600
    },
     {
        "id": 20,
        "nombre": "Cámara de seguridad",
        "cantidad": 6,
        "precio": 120
    },
     {
        "id": 21,
        "nombre": "Proyector",
        "cantidad": 4,
        "precio": 300
    },
     {
        "id": 22,
        "nombre": "Lentes de realidad virtual",
        "cantidad": 2,
        "precio": 200
    },
    {
        "id": 23,
        "nombre": "Barra de sonido",
        "cantidad": 9,
        "precio": 250
    },
    {
        "id": 24,
        "nombre": "Lámpara inteligente",
        "cantidad": 13,
        "precio": 70
    },
    {
        "id": 25,
        "nombre": "Cable HDMI",
        "cantidad": 40,
        "precio": 10
    },
    {
        "id": 26,
        "nombre": "Adaptador de corriente",
        "cantidad": 15,
        "precio": 20
    },
    {
        "id": 27,
        "nombre": "Cámara web",
        "cantidad": 7,
        "precio": 80
    },
     {
        "id": 28,
        "nombre": "Batería externa",
        "cantidad": 25,
        "precio": 40
    },
    {
        "id": 29,
        "nombre": "Auriculares con cancelación de ruido",
        "cantidad": 10,
        "precio": 200
    },
    {
        "id": 30,
        "nombre": "Memoria USB",
        "cantidad": 50,
        "precio": 15
    },
    {
        "id": 31,
        "nombre": "Lector de tarjetas",
        "cantidad": 12,
        "precio": 15
    },
     {
        "id": 32,
        "nombre": "Pantalla táctil",
        "cantidad": 3,
        "precio": 300
    },
     {
        "id": 33,
        "nombre": "Cámara de acción",
        "cantidad": 5,
        "precio": 150
    },
    {
        "id": 34,
        "nombre": "Escáner",
        "cantidad": 6,
        "precio": 100
    },
    {
        "id": 35,
        "nombre": "Drone",
        "cantidad": 2,
        "precio": 500
    },
    {
        "id": 36,
        "nombre": "Cable USB-C",
        "cantidad": 30,
        "precio": 8
    },
    {
        "id": 37,
        "nombre": "Estación de carga",
        "cantidad": 10,
        "precio": 60
    },
{
        "id": 38,
        "nombre": "Tarjeta gráfica",
        "cantidad": 4,
        "precio": 800
    },
    {
        "id": 39,
        "nombre": "Mousepad",
        "cantidad": 20,
        "precio": 15
    },
     {
        "id": 40,
        "nombre": "Teclado inalámbrico",
        "cantidad": 15,
        "precio": 70
    },
    {
        "id": 41,
        "nombre": "Micrófono USB",
        "cantidad": 8,
        "precio": 90
    },
    {
        "id": 42,
        "nombre": "Memoria RAM",
        "cantidad": 10,
        "precio": 150
    },
    {
        "id": 43,
        "nombre": "Soporte para teléfono",
        "cantidad": 15,
        "precio": 20
    },
    {
        "id": 44,
        "nombre": "Kit de limpieza para electrónicos",
        "cantidad": 25,
        "precio": 30
    },
    {
        "id": 45,
        "nombre": "Cable de audio",
        "cantidad": 30,
        "precio": 5
    },
    {
        "id": 46,
        "nombre": "Base de carga inalámbrica",
        "cantidad": 12,
        "precio": 40
    },
     {
        "id": 47,
        "nombre": "Reproductor de Blu-ray",
        "cantidad": 5,
        "precio": 100
    },
     {
        "id": 48,
        "nombre": "Alarma de seguridad",
        "cantidad": 8,
        "precio": 120
    },
     {
        "id": 49,
        "nombre": "Impresora 3D",
        "cantidad": 3,
        "precio": 500
    },
    {
        "id": 50,
        "nombre": "Cable VGA",
        "cantidad": 20,
        "precio": 10
    }
]
@app.route("/")
def hello_world():
    return render_template('login.html')    

@app.route('/home/<name>')
def home(name):
    return f'Welcome to the home {escape(name)}'



@app.route('/prods')
def login():
    return render_template('prods.html', prod = allProducts)


@app.route('/details/<id>') 
def details(id):
    return render_template("details.html", productoDetail = allProducts[int(id) -1])

if __name__ == '__main__':
    app.run(debug=True)