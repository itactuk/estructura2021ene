
# no existen como tal en python
# Las tuplas no son arreglos, porque son objetos más complejos que los arreglos

# las tuplas son más ligeras que las listas y no pueden cambiar su tamaño

frutas = ("Manzana", "Fresa", "Pera", "Banana")

# no es permitido usar append o add
# frutas.append("Molondrón")
# frutas.add("Molondrón")

# imprime dirección de memoria a la que apunta la variable
print(f"Id frutas: {id(frutas)} antes de concat")

# esto es más ineficiente que add/append. Por qué?
frutas = frutas + ("Uva", )  # O(n), siendo n el numero de elementos de la nueva tupla
print(frutas)

# imprime dirección de memoria a la que apunta la variable
print(f"Id frutas: {id(frutas)} después de concat")

# por qué varía la dirección de memoria?

