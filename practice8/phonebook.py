from connect import connect

# Call function
def search_contacts(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Call procedure (upsert)
def upsert(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()

    cur.close()
    conn.close()


# Call delete
def delete(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()

    cur.close()
    conn.close()


# TEST
if __name__ == "__main__":
    upsert("Ali", "87771234567")
    search_contacts("Ali")
    delete("Ali")