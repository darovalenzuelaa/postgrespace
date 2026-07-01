import psycopg2

conn = psycopg2.connect(
    host="postgres",      # Codespaces: "postgres" | Local: "localhost"
    database="veterinariadb",
    user="postgres",
    password="1234"
)
cursor = conn.cursor()

print("=== Buscador de tutores (versión segura) ===")
nombre = input("Nombre del tutor: ")

# %s le dice a psycopg2: "este valor viene de afuera, trátalo como dato, no como SQL"
cursor.execute(
    "SELECT id_tutor, nombre, telefono FROM tutores WHERE nombre = %s",
    (nombre,)
)

resultados = cursor.fetchall()

if resultados:
    for fila in resultados:
        print(f"  id={fila[0]}  nombre={fila[1]}  tel={fila[2]}")
else:
    print("Ningún tutor encontrado.")

cursor.close()
conn.close()
