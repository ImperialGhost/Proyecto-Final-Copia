from flask import Flask, render_template, request, redirect, url_for
from entities.producto import Producto
from entities.pedido_total import Pedido
from enums.tipo_producto import Tipo_producto
from exceptions.cantidad_invalida import Cantidad_invalida

app = Flask(__name__)

MENU = {
    1: Producto(1, "Donitas", 25.0, Tipo_producto.POSTRE),
    2: Producto(2, "Cocacola", 26.0, Tipo_producto.BEBIDA),
    3: Producto(3, "Sandwich", 33.0, Tipo_producto.COMIDA),
    4: Producto(4, "Chicles", 12.0, Tipo_producto.OTRO)
}

pedido_actual = Pedido()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', productos=MENU.values())

@app.route('/agregar/<int:id_producto>', methods=['POST'])
def agregar_producto(id_producto):
    try:
        cantidad = int(request.form.get('cantidad', 0))
        
        if cantidad <= 0:
            raise Cantidad_invalida(f"No puedes agregar {cantidad} productos.")
        
        producto = MENU.get(id_producto)
        if producto:
            pedido_actual.agregar_item(producto, cantidad)
            
    except Cantidad_invalida as e:
        print(f"Error: {e.message}")
        
    return redirect(url_for('menu'))

@app.route('/ticket')
def ticket():
    return render_template('ticket.html', pedido=pedido_actual)

@app.route('/limpiar')
def limpiar_pedido():
    pedido_actual.productos.clear() 
    return redirect(url_for('menu'))

if __name__ == '__main__':
    app.run(debug=True)