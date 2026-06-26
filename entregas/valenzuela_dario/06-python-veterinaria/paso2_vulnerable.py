import psycopg2

conn = psycopg2.connect(
    host="postgres",      # Codespaces: "postgres" | Local: "localhost"
    database="veterinariadb",
    user="postgres",
    password="1234"
)
cursor = conn.cursor()

print("=== Buscador de tutores ===")
nombre = input("Nombre del tutor: ")

# Construye la consulta pegando el input directamente
query = f"SELECT id_tutor, nombre, telefono FROM tutores WHERE nombre = '{nombre}'"

print(f"\nConsulta que se ejecuta:\n  {query}\n")

cursor.execute(query)
resultados = cursor.fetchall()

if resultados:
    for fila in resultados:
        print(f"  id={fila[0]}  nombre={fila[1]}  tel={fila[2]}")
else:
    print("Ningún tutor encontrado.")

cursor.close()
conn.close()
