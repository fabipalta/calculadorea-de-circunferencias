import urllib.parse                                                 #se impórta de la libreria urllib.parse que sirven basicamente para manipular URL'S a voluntad
import requests                                                     #se importa de la libreria requests que sirven para conocer la informacion que pasa del navegaor al cliente

medida_km = "k"                                                                     #la variable medida_km se especifica en la url de mas abajo e indica que la unidad de medida de la distancia sera en kilometros
idioma = "es_MX"                                                                    #la variable idioma sera introducia en la url mas abajo para poder seleccionar el idioma español mexico
main_api = "https://www.mapquestapi.com/directions/v2/route?"                       #tambien se especifica la api que se utilizara obtenida en la paguina web mapquest.com
key = "3KJjpKrviS0rrfj6Xzw7zjcAgLPyDhpj"                                            #se especifica la key que fue conseguida en mapquest.com
#bucle
while True:                                                                     #el bucle while(mientras) se originara al inicio del codigo y en el estara la mayoria del cuerpo de este mismo
    origen = input("Ingrese el origen ('salida' para terminar): ")                      #en la variable origen se le pide al usuario que ingrese un origen y se le indica las credenciales que necesita para poder salir el programa
    if origen.lower() == "s":                                                         #el comando origen.lower es un comando utlizado para tranformar las letras mayusculas a minusculas y asi asegurarse que se cumpla con la salida"s"
        break                                                                          #el comano break se usa para quebrar el bucle en caso de que se cumpla con la condicion if de la linea anterior
    
    destino = input("Ingrese el destino ('salida' para terminar): ")                    #en la variable destino se le pide al usuario ingresar un destino y se le especifica las credenciales que debe utilizar para salir del programa
    if destino.lower() == "s":                                                           #de igual manera que en el origen el destino esta acompañao de un .lower para asegurar la salia "s"
        break                                                                           #si se cumplen las creenciales se rompera el bucle y se saldra el programa
    
    url = main_api + urllib.parse.urlencode({"key": key, "from": origen, "to": destino, "unit": medida_km, "locale": idioma})       #la variable url contiene la api y se llama a urllib.parse para poder llamar a partes especificas y generar una url con solo lo que necesitemos
    json_data = requests.get(url).json()                                                    #la variable json_data contiene los requests que llamaran a la url que antes especificamos
    distancia = json_data["route"]["distance"]                                              #la variable contiene a json_ata para poer obtener informacion especifica de ella, tal como, la ruta y la distancia
    distancia_redondeada = round(distancia, 1)                                              #esta variable fue creada para redonear la distancia final a 1 decimal
    tiempo = json_data["route"]["time"]                                                     #en la variable tiempo se de toma json_data la ruta y el tiempo 
   

    horas = tiempo // 3600                                                                 #esta seccion se especifican en la variable horas la conversion del tiempo  divido en 3600 segundos
    minutos = (tiempo % 3600) // 60                                                        #de la misma manera de calcula los minutos del resultao anterior(tiempo) y luego se divide en 60 que vendrian siendo los minutos
    segundos = tiempo % 60                                                                 # los segundos no son la excepcion y se calcula el resultado anterior (tiempo) por 60 que son los segundos

    print("Distancia:", distancia_redondeada, "kilometros")                                 #se imprimen la distancia que fue redondedada con anterioridad
    print("Duración del viaje:", int(horas), "horas,", int(minutos), "minutos,", int(segundos), "segundos")             #se imprime tambien el tiempo de viaje que tomara segun la distancia y de igual manera llamando a dichas variables

    maniobras = json_data['route']['legs'][0]['maneuvers']                              #se define la variable maniobras  y se incluye json_data para llamar la ruta, pies y maniobras
    print("Indicaciones de giro:")                                                      #se imprime la palabra indicaciones de giro para dar inicio a estas y se vea de una manera mas ordenada y limpia
    for step in maniobras:                                                               #luego se inicia un bucle donde recorrera todos los pasos que se debe de seguir    
       print("*", step["narrative"])                                                    #luego se imprimira todos los pasos que logre recopilar el codigo hasta llegar al destino deseado. en este punto termina el codigo y vuelve al incio para consultar mas direcciones de origen y destino


