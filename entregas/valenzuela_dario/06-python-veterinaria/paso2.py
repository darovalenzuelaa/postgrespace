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



-- FETCHONE()

conn = psycopg2.connect(
    host="postgres",      # Codespaces: "postgres" | Local: "localhost"
    database="veterinariadb",
    user="postgres", password="1234"
)
cursor = conn.cursor()

tutor_id = 1

cursor.execute("""
    SELECT t.nombre,
           COUNT(cv.id_consulta)          AS consultas,
           COALESCE(SUM(cv.costo), 0)     AS total_gastado
    FROM tutores t
    LEFT JOIN consultas_veterinarias cv ON cv.tutor_id = t.id_tutor
    WHERE t.id_tutor = %s
    GROUP BY t.nombre;
""", (tutor_id,))

fila = cursor.fetchone()   # una sola tupla, o None si no hay resultado

if fila:
    nombre, consultas, total = fila
    print(f"Tutor:     {nombre}")
    print(f"Consultas: {consultas}")
    print(f"Total:     ${total:.2f}")
else:
    print("Tutor no encontrado")

cursor.close()
conn.close()

cursor.close()
conn.close()
