def pagonomina(dic):
    diccionario = dict()
    for empleado in dic:
        key = empleado
        nombres = dic[empleado]["nombres"]
        apellidos = dic[key]["apellidos"]
        horas = dic[key]["horas"]
        horasext = dic[key]["horasExtras"]
        remuneracion = dic[key]["remuneracion"]
        pago = (horas * remuneracion["pagoshoras"] + horasext * remuneracion["pagoshoraextra"])+remuneracion['bonos']+remuneracion['subsidio']
        ref = nombres[0].upper()+apellidos[0].upper()+str(key)
        diccionario[key] = {
            'nombres': nombres,
            'apellidos': apellidos,
            'remuneracion': pago,
            'referencia': ref 
        }
    return diccionario


print(pagonomina(
    {
        1102856334:{
            'nombres': "jose gregor",
            'apellidos': "santos rico",
            'horas': 42,
            'horasExtras': 8,
            'remuneracion': {
                'pagoshoras': 13000,
                'pagoshoraextra': 26000,
                'bonos': 50000,
                'subsidio': 150000     
            }
        },
        71856789:{
            'nombres': "sergio luis",
            'apellidos': "monsalvo llorente",
            'horas': 36,
            'horasExtras': 16,
            'remuneracion': {
                'pagoshoras': 16000,
                'pagoshoraextra': 26000,
                'bonos': 100000,
                'subsidio': 150000     
            }
        }
     }
))


