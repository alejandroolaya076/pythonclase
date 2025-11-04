"Funcion convencional"
def area(b,a):
    return (b*a)/2
print(area(5,5))


"Funcion lambda"
area2 = lambda b,a:(b*a)/2
print(area2)

"Funcion filter (selecciona y devuelve los elementos que cumplen la condicion)"
numeros=[1,2,3,4,5]
filtrar=filter(lambda x:x>3,numeros)
print(list(filtrar))

"Funcion map  (recorre la lista y aplica la funcion a cada elemento, el map puede crear una nueva lista)"
elevar=map(lambda x:x**2,numeros)
print(list(elevar))

"Funcion regex (expresiones regulares) patrones de texto para buscar, validar o manipular cadenas de texto"
import re 
cadena="Vean a ver si llegan temprano, dejen de buscar lo que no se les ha perdido"
print(re.search("ñero",cadena))
patron = r"\\w*"
result=re.findall(patron,cadena)
print(result)
cambio=re.sub(r"\s","#", cadena)
print(cambio)
partres=cadena.split()
print(partres)
