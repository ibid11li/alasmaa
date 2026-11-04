from database import get_connection


def search_names(gender="", letters=None, search_letter=""):

    query = "SELECT name, meaning FROM names WHERE 1=1"
    params = []

    if gender:
        query += " AND gender = %s"
        params.append(gender)

    if letters is not None:
        query += " AND CHAR_LENGTH(name) = %s"
        params.append(letters)

    if search_letter:
        query += " AND name LIKE %s"
        params.append("%" + search_letter + "%")

    connection = get_connection()

    try:
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(query, tuple(params))
            results = cursor.fetchall()
            return results

        finally:
            cursor.close()

    finally:
        connection.close()
