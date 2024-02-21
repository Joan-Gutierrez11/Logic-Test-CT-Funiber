from pprint import pprint

## Sonidos animales
# Rana: brr, birip, brrah, croac
# Libélula: fiu, plop, pep
# Grillo: cric-cric, trri-trri, bri-bri

## Canciones
# brr, fiu, cric-cric, brrah
# pep, birip, trri-trri, croac
# bri-bri, plop, cric-cric, brrah

def crear_diccionario_sonidos(sonidos: list, num_canciones: int):
    sonidosD = {}
    for _sonido in sonidos:
        sonidosD[_sonido] = [ -1 for i in range(num_canciones) ]
    return sonidosD

def crear_secuencia_musical(sonidosD: dict, canciones: list):
    for i in range(len(canciones)):
        _cancion = canciones[i]
        for idx in range(len(_cancion)):
            _sonido_cancion = _cancion[idx]
            sonidosD[_sonido_cancion][i] = idx

def obtener_secuencia(sonidosD: dict, canciones: list, sonido: str):
    indices = sonidosD.get(sonido, None)
    if not indices:
        raise Exception("No existe una cancion que tenga ese sonido")

    idx_cancion = -1
    idx_sonido_en_cancion = -1

    for i in range(len(indices)):
        if indices[i] != -1:
            idx_cancion = i
            idx_sonido_en_cancion = indices[i]
    
    if idx_cancion == -1 or idx_sonido_en_cancion == -1:
        raise Exception("Ese sonido no pertenece a ninguna cancion")
    
    cancion_reprod = canciones[idx_cancion]
    if idx_sonido_en_cancion >= len(cancion_reprod)-1:
        return []
    return cancion_reprod[idx_sonido_en_cancion+1:]

# Programa principal

def main():
    # Sonidos
    rana = ['brr', 'birip', 'brrah', 'croac']
    libelula = ['fiu', 'plop', 'pep']
    grillo = ['cric-cric', 'trri-trri', 'bri-bri']
    
    # Canciones
    cancion1 = ['brr', 'fiu', 'cric-cric', 'brrah']
    cancion2 = ['pep', 'birip', 'trri-trri', 'croac']
    cancion3 = ['bri-bri', 'plop', 'cric-cric', 'brrah']

    canciones = [cancion1, cancion2, cancion3]
    sonidos = rana+libelula+grillo

    D = crear_diccionario_sonidos(sonidos, len(canciones))
    crear_secuencia_musical(D, canciones)
    pprint(D)

    sonido_usuario = input('Ingrese un sonido: ')

    try:
        secuencia = obtener_secuencia(D, canciones, sonido_usuario)
        if len(secuencia) < 1:
            print('...')
            return
            
        print(', '.join(secuencia))
    except Exception as e:
        print(e)

main()