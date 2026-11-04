
import csv
import sys
import mysql.connector
from database import get_connection

# دعم طباعة العربية
sys.stdout.reconfigure(encoding="utf-8")

clean_names = []
seen = set()

# قراءة وتنظيف البيانات
with open("names.csv", "r", encoding="utf-8-sig", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = (row.get("name") or "").strip()
        gender = (row.get("gender") or "").strip().lower()
        meaning = (row.get("meaning") or "").strip()

        if not name or not meaning or gender not in ("male", "female"):
            print("Invalid data:", row)
            continue

        key = (name, gender)

        if key in seen:
            print("Duplicate:", name)
            continue

        seen.add(key)
        clean_names.append((name, gender, meaning))


print("Valid names:", len(clean_names))

# تحميل البيانات إلى TiDB Cloud
if clean_names:

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO names (name, gender, meaning)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE id = id
            """

            cursor.executemany(query, clean_names)

            connection.commit()

            print("Import completed successfully!")

        finally:
            cursor.close()

    except mysql.connector.Error as error:
        if connection is not None:
            connection.rollback()

        print("Database error:", error)

    finally:
        if connection is not None:
            connection.close()

else:
    print("No valid names to import.")
