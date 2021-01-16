

def contar_digitos_consecutivos(texto: str) -> int:  # -> indica valor de retorno. En este caso, int
    """
    "34342jjkl43jj43kjl43"
    "fsdfsd3535fdsfsd"
    "fdsfsd434"
    :param texto:
    :return:
    """
    contador = 0
    # for i in range(len(texto))
    # c = texto[i]
    # for i in range(0, len(texto))
    # for c in texto:
    for i in range(len(texto)):
        c = texto[i]
        c_a = None
        c_s = None
        if i > 0:
            c_a = texto[i-1]
        if i < len(texto) - 1:  # "hola"   -> len(texto)=4   text[0]=h, texto[1]="o", texto[2]=l, texto[3]=o
            c_s = texto[i+1]
        if c.isdigit():
            es_consecutivo = False
            if c_a is not None and c_a.isdigit():
                es_consecutivo = True
            if c_s is not None and c_s.isdigit():
                es_consecutivo = True
            if es_consecutivo:
                contador += 1
    return contador

