"""{
   1102856334: {
       'nombres': "jose gregor",
        'apellidos': "santos rico",
        'remuneracion': 904000,
        'referencia': 'JS1102856334' 
   },
   71856789:{
            'nombres': "sergio luis",
            'apellidos': "monsalvo llorente", 
            'remuneracion': 1142000,
            'referencia': 'SM71856789'
   },
   'pago_total': 2046000
}"""

def pagonomina(dic):
    empleados = dict()
    for empleado in dic:
        nombres = dic.get(empleado).get('nombres')
        apellidos = dic[empleado].get('apellidos')
        rem = dic[empleado].get('remuneracion')
        pago = (dic[empleado].get('horas')*rem['pagoshoras'] + dic[empleado].get('horasExtras')*rem['pagoshoraextra'])+rem['subsidio']+rem['bonos']
        ref = f"{nombres[0].upper() + apellidos[0].upper()}{empleado}"
        empleados[empleado] = {
            'nombres': nombres,
            'apellidos': apellidos,
            'remuneracion': pago,
            'referencia': ref
        }
    return empleados

diccionario = {
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

nomina = pagonomina(diccionario)     
print(nomina)
