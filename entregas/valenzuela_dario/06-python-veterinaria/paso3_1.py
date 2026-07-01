import psycopg2

conn = psycopg2.connect(
    host="postgres",      # Codespaces: "postgres" | Local: "localhost"
    database="veterinariadb",
    user="postgres",
    password="1234"
)
cursor = conn.cursor()

# INSERT con RETURNING para obtener el id generado por el SERIAL
cursor.execute("""
    INSERT INTO mascotas (nombre, especie, edad_meses, tutor_id)
    VALUES (%s, %s, %s, %s)
    RETURNING id_mascota;
""", ("Thor", "Perro", 6, 2))

id_nuevo = cursor.fetchone()[0]
conn.commit()

print(f"Mascota registrada con id: {id_nuevo}")

cursor.close()
conn.close()
