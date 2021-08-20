""" 
{
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
            'referencia': SM71856789
   }
   pago_total: 2046000
}

"""

def pagonomina(dic):
    empleados = dict()
    nomina = 0
    for emp in dic:
        nombres = dic[emp]['nombres']
        apellidos = dic[emp]['apellidos']
        rem = dic[emp]['remuneracion']
        pago = (dic[emp]['horas'] * rem['pagoshoras'] + dic[emp]['horasExtras'] * rem['pagoshoraextra']) + rem['bonos'] + rem['subsidio']
        ref = nombres[0].upper()+apellidos[0].upper()+str(emp)
        nomina += pago
        empleados[emp] = {
            'nombres': nombres,
            'apellidos': apellidos,
            'remuneracion': pago,
            'referencia': ref
        }
    empleados['pago_total'] = nomina
    return empleados

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

