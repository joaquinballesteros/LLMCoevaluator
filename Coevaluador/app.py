from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import unicodedata
import datetime

app = Flask(__name__)
# Corregido: Definimos solo el nombre del archivo, no la ruta completa
FICHERO_CORRECCIONES = "Calificaciones.csv"  
LENGUAJE = ".c"                          
CARPETA_BASE = "./C/pruebas/"            

def normalize_string(s):
    s = s.lower()
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    s = s.split("_")[0]
    return s

@app.route('/')
def index():
    carpetas = sorted([f for f in os.listdir(CARPETA_BASE) if os.path.isdir(os.path.join(CARPETA_BASE, f))])
    return render_template("index.html", carpetas=carpetas)

@app.route('/load', methods=['POST'])
def load_data():
    data = request.json
    carpeta = data['carpeta']
    path = os.path.join(CARPETA_BASE, carpeta)
    archivos = []
    
    # Recopilar todos los archivos con la extensión deseada
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(LENGUAJE):
                relpath = os.path.relpath(os.path.join(root, file), path)
                archivos.append(relpath)
    
    archivos.sort()
    
    # Crear la lista de objetos con nombre y contenido
    archivos_con_contenido = []
    for f in archivos[:10]:  # Limitar a los 10 primeros archivos
        ruta = os.path.join(path, f)
        try:
            with open(ruta, 'r', encoding='utf-8') as file:
                contenido = file.read()
                archivos_con_contenido.append({
                    "nombre": f,  # Nombre relativo del archivo
                    "contenido": contenido
                })
        except Exception as e:
            archivos_con_contenido.append({
                "nombre": f,
                "contenido": f"Error al leer {f}: {str(e)}"
            })
    
    # Cargar el HTML de retroalimentación
    html_path = os.path.join(path, "Resultado.html")
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_code = f.read().replace("<br>", "\\n")
    except:
        html_code = "<p>No se encontró el archivo HTML.</p>"
    
    # Obtener la nota
    nota = obtener_nota(carpeta)
    print(f"Nota obtenida: {nota}")
    
    # Último guardado (archivo timestamp si existe)
    timestamp_path = os.path.join(path, "ultimo_guardado.txt")
    ultimo_guardado = None
    if os.path.exists(timestamp_path):
        try:
            with open(timestamp_path, "r") as f:
                ultimo_guardado = f.read().strip()
        except:
            ultimo_guardado = None
    
    return jsonify({
        "archivos": archivos_con_contenido,
        "html": html_code,
        "nota": nota,
        "ultimoGuardado": ultimo_guardado,
        # Añadir para depuración
        "csv_path": os.path.join(CARPETA_BASE, FICHERO_CORRECCIONES)
    })

@app.route('/save', methods=['POST'])
def save_data():
    data = request.json
    carpeta = data['carpeta']
    html = data['html']
    nota = data['nota']
    
    carpeta_path = os.path.join(CARPETA_BASE, carpeta)
    html_path = os.path.join(carpeta_path, "Resultado.html")
    
    # Guardar HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    # Guardar timestamp
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    timestamp_path = os.path.join(carpeta_path, "ultimo_guardado.txt")
    with open(timestamp_path, "w") as f:
        f.write(timestamp)
    
    print(f"Carpeta: {carpeta}")
    print(f"Nota: {nota}")
    print(f"HTML: {html[:100]}...")  # Muestra solo los primeros 100 caracteres para no saturar la salida
    
    # Guardar en CSV
    guardar_csv_completo(nota, carpeta, html)
    
    return jsonify({
        "message": "Guardado correctamente.",
        "timestamp": timestamp,
        "csv_path": os.path.join(CARPETA_BASE, FICHERO_CORRECCIONES)  # Para depuración
    })

def obtener_nota(estudiante):
    # Corregido: Construimos correctamente la ruta al archivo CSV
    csv_path = os.path.join(CARPETA_BASE, FICHERO_CORRECCIONES)
    print(f"Obteniendo nota para {estudiante} desde {csv_path}")
    
    if not os.path.exists(csv_path):
        print(f"El archivo CSV no existe: {csv_path}")
        return ""
    
    try:
        df = pd.read_csv(csv_path, encoding='utf-8-sig')
        print(f"CSV leído correctamente. Columnas: {df.columns.tolist()}")
    except Exception as e:
        print(f"Error al leer CSV: {e}")
        return ""
    
    norm_student = normalize_string(estudiante)
    print(f"Estudiante normalizado: {norm_student}")
    
    # Verificar si 'Nombre completo' existe en las columnas
    if 'Nombre completo' not in df.columns:
        print(f"ERROR: 'Nombre completo' no existe en las columnas del CSV: {df.columns.tolist()}")
        return ""
    
    df["norm_nombre"] = df["Nombre completo"].apply(lambda x: normalize_string(str(x)))
    matching = df[df['norm_nombre'].str.contains(norm_student, case=False, na=False)]
    
    if not matching.empty:
        if "Calificación" in matching.columns:
            nota = str(matching.iloc[0]["Calificación"])
            print(f"Nota encontrada: {nota}")
            return nota
        else:
            print(f"ERROR: 'Calificación' no existe en las columnas: {matching.columns.tolist()}")
    else:
        print(f"No se encontró al estudiante {norm_student} en el CSV")
    
    return ""

def guardar_csv_completo(nota, carpeta, html_code):
    # Corregido: Construimos correctamente la ruta al archivo CSV
    csv_path = os.path.join(CARPETA_BASE, FICHERO_CORRECCIONES)
    print(f"Guardando en CSV: {csv_path}")
    
    if not os.path.exists(csv_path):
        print(f"El archivo CSV no existe: {csv_path}")
        return
    
    try:
        df = pd.read_csv(csv_path, encoding='utf-8-sig')
        print(f"CSV leído correctamente para guardar. Columnas: {df.columns.tolist()}")
    except Exception as e:
        print(f"Error al leer CSV para guardar: {e}")
        return
    
    norm_student = normalize_string(carpeta)
    print(f"Estudiante normalizado para guardar: {norm_student}")
    
    if 'Nombre completo' not in df.columns:
        print(f"ERROR: 'Nombre completo' no existe en las columnas del CSV: {df.columns.tolist()}")
        return
    
    df["norm_nombre"] = df["Nombre completo"].apply(lambda x: normalize_string(str(x)))
    
    if norm_student not in df["norm_nombre"].values:
        print(f"El estudiante {norm_student} no se encuentra en el CSV.")
        return
    
    # Formatear nota y guardar
    try:
        nota_format = str(nota).replace(".", ",")
        print(f"Guardando nota: {nota_format} para estudiante: {norm_student}")
        
        # Verificar si las columnas existen
        if "Calificación" not in df.columns:
            print(f"ERROR: 'Calificación' no existe en las columnas: {df.columns.tolist()}")
            return
            
        if "Comentarios de retroalimentación del profesor" not in df.columns:
            print(f"ERROR: 'Comentarios de retroalimentación del profesor' no existe")
            return
        
        df.loc[df["norm_nombre"] == norm_student, "Calificación"] = nota_format
        df.loc[df["norm_nombre"] == norm_student, "Comentarios de retroalimentación del profesor"] = html_code.replace("\\n", "<br>")
        
        df.drop(columns=["norm_nombre"], errors='ignore', inplace=True)
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"CSV guardado correctamente")
    except Exception as e:
        print(f"Error al guardar en CSV: {e}")

if __name__ == '__main__':
    app.run(debug=True)