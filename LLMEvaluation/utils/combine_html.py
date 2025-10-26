import os
from bs4 import BeautifulSoup

# 1. Configuración: carpeta raíz donde están las subcarpetas de cada usuario
ROOT_DIR = "./LLMEvaluation/courses/objectOrientedProgramming/assesments/Caidas/students"   # <- cámbialo a tu ruta

# 2. Lista de ficheros HTML a procesar (puedes añadir o quitar nombres aquí, este es el orden en el que se mostrarán, lo ideal, igual que en el examen.)
result_files = [
    "ResultCaidaException.html",
    "ResultFracturaAsociada.html",
    "ResultNotificable.html",
    "ResultEvento.html",
    "ResultMovimientoBrusco.html",
    "ResultAmagoCaida.html",
    "ResultCaidaConfirmada.html",
    "ResultUsuarioVigilado.html",
    "ResultSistemaDeteccion.html"
]

# 3. Encabezado de la tabla de salida
TABLE_HEADER = '''<table border="1">
  <tr>
    <th>Clase</th>
    <th>Puntuación</th>
    <th>Retroalimentación</th>
  </tr>
'''

def process_user_folder(user_path):
    rows = []
    for fname in result_files:
        fpath = os.path.join(user_path, fname)
        if not os.path.isfile(fpath):
            continue
        with open(fpath, encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            trs = soup.find_all('tr')
            for tr in trs:
                rows.append(str(tr))


    if not rows:
        # nada que combinar
        return

    # Montamos el HTML completo
    combined = TABLE_HEADER + "\n".join(rows) + "\n</table>"

    # Guardamos el resultado
    out_path = os.path.join(user_path, 'Result.html')
    with open(out_path, 'w', encoding='utf-8') as out:
        out.write(combined)
    print(f'→ creado: {out_path}')

def main():
    # Recorremos todas las entradas en ROOT_DIR
    for entry in os.listdir(ROOT_DIR):
        user_dir = os.path.join(ROOT_DIR, entry)
        if os.path.isdir(user_dir):
                # Procesamos la carpeta del usuario
            process_user_folder(user_dir)

if __name__ == '__main__':
    main()
