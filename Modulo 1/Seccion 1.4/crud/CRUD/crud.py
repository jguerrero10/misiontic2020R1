import openpyxl as op
import datetime as dt

""" 
CRUD Basico - Excel (BD)
"""

def crear_info(archivo, datos):
    libro = op.Workbook()
    hoja = libro.active
    col = 1
    for i in datos:
        hoja.cell(row=1, column=col, value=i)
        col += 1
    libro.save(archivo)

def create(archivo, datos):
    libro = op.load_workbook(archivo)
    hoja = libro.active
    fila = hoja.max_row + 1
    col = 1
    fecha = dt.datetime.now()
    for i in datos:
        hoja.cell(row=fila, column=col, value=i)
        col += 1
    hoja.cell(row=fila, column=hoja.max_column, value=fecha)
    libro.save(archivo)

def read(archivo, info):
    libro = op.load_workbook(archivo)
    hoja = libro.active
    datos = dict()
    enc = list()
    if info.lower() == "todos":
        for row in hoja.iter_rows(min_row=1, max_col=hoja.max_column, max_row=1):
            for celda in row:
                enc.append(celda.value)   
        for row in hoja.iter_rows(min_row=2, max_col=hoja.max_column, max_row=hoja.max_row):
            info = dict()
            for i in range(0, len(row)):
                info[enc[i]] = row[i].value
            datos[row[0].value] = info
    # Aqui else para recupera solo un valor
    return datos