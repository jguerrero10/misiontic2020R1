## Enunciado
Usted se encuentra laborando en una empresa llamada "Servitap sas", el jefe de nómina le ha encargado a usted diseñar un programa en Python, una función que reciba la información de cada trabajador, esta información se encuentra en un diccionario donde las claves son los números de identificación del trabajador, el cual contiene la siguiente información o campos:

| Clave             | Type(Valor) | Valor (estructura) / descripción| 
|-------------------|-------------|-----------------------------|
| nombres           | str         | {primer nombre} {segundo nombre}| 
| apellidos         | str         | {primer apellido} {segundo apellido}|
| horas             | int         | Horas trabajadas en el mes 
| horasExtras       | int         | Horas trabajadas en el mes| 
| remuneracion      | int         | contiene pagohoras, pagohorasextra, bonos, subsidios|

El requerimiento es realizar una función que retorne un diccionario con clave el número de identificación del trabajado, y el valor un diccionario que contenga el nombre, apellidos, remuneración total, referencia de pago que es la primera letra en mayuscula del primer nombre y del apellido mas el numero de identificación. Además, una clave adicional con la totalidad a pagar a toda la nómina.

    pagonomina(
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
    )

### Estructura de la Salida

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
    }