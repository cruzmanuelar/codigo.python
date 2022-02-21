productos = [
    {
        "Producto": "Cebolla",
        "Cantidad": 12,
    },
    {
        "Producto": "Tomate",
        "Cantidad": 40,
    }
]

linea = '------------------------------------------------'

def agregarProducto():
    
    print('-----------DATOS DE NUEVO PRODUCTO--------------')
    nombreProducto = input('Ingrese nombre: ')
    cantidadProducto = int(input('Ingrese cantidad: '))

    nuevo = {'Producto': nombreProducto, 'Cantidad': cantidadProducto}
    productos.append(nuevo)
    print('Producto agregado!')
    print(linea)

def mostrarProductos():

    i = 1
    print('------------------PRODUCTOS---------------------')
    for x in productos:
        print( str(i) + '. Nombre: ' + x['Producto'] + ', cantidad: ' + str(x['Cantidad']))
        i = i + 1    
    print(linea)

def eliminarProducto():

    mostrarProductos()
    
    indice = int(input('Escriba el indice de producto a eliminar: '))
    productos.pop(indice - 1)
    print('Producto eliminado!')
    print(linea)

def editarProducto():

    mostrarProductos()
    indice = int(input('Escriba el indice de producto a editar: '))

    nombreNuevo = input('Nombre nuevo: ')
    cantidadNuevo = int(input('Cantidad nuevo: '))
    productos[indice - 1]['Producto'] = nombreNuevo
    productos[indice - 1]['Cantidad'] = cantidadNuevo
    print('Producto editado!')
    print(linea)

opcion = 1
while opcion != 0:
    print('1. Mostrar productos')
    print('2. Agregar producto')
    print('3. Editar producto')
    print('4. Eliminar producto')
    print('0. Salir')
    opcion = int(input('Ingrese opcion: '))
    if(opcion == 1):
        mostrarProductos()
    elif(opcion == 2):
        agregarProducto()
    elif(opcion == 3):
        editarProducto()
    elif(opcion == 4):
        eliminarProducto()
    elif(opcion == 0):
        print('Adios')
    else:
        print('Opcion no valida')