meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "SHEESH":"una ligera desaprobacion" ,
            "CREEPY":"aterrador,siniestro" ,
            "TO AGGRO":"ponerse agresivo" ,
            }
            
            
while True:
    word = input("escribe una palabra que no esntiendas con mayusculas")
    
    if word in meme_dict.keys():
        print(word,":",meme_dict[word])
    else:
        print("No se ha encontrado esa palabra")
