#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector
#main routine for displaying search results
#will take in values from html, and run the corresponding query
#passes JSON values back
def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')
    col = form.getvalue('column_term')
    #Test Term: "U43746.1"
    conn = mysql.connector.connect(user='jnguye36', password='J0n!7301991', host='localhost', database='jnguye36')
    cursor = conn.cursor()

    if col == "name":
        qry = """
              SELECT name, a, g, c, t, gc, purine, pyrimidine, length, date
                FROM final
               WHERE name LIKE %s
        """
        cursor.execute(qry, ('%' + term + '%',))
    if col == "gc":
        upper = int(int(term) + 5)
        lower = int(int(term) - 5)
        qry = """
              SELECT name, a, g, c, t, gc, purine, pyrimidine, length, date
                FROM final
               WHERE gc >= %s AND gc <= %s
        """
        cursor.execute(qry, (lower, upper))        
    if col == "purine":
        upper = int(int(term) + 5)
        lower = int(int(term) - 5)
        qry = """
              SELECT name, a, g, c, t, gc, purine, pyrimidine, length, date
                FROM final
               WHERE purine >= %s AND purine <= %s
        """
        cursor.execute(qry, (lower, upper))   
    if col == "pyrimidine":
        upper = int(int(term) + 5)
        lower = int(int(term) - 5)
        qry = """
              SELECT name, a, g, c, t, gc, purine, pyrimidine, length, date
                FROM final
               WHERE pyrimidine >= %s AND pyrimidine <= %s
        """
        cursor.execute(qry, (lower, upper))   


    results = {"match_count":0, "matches":list()}
    for (fasta_id, a, g, c, t, gc, pur, pyr, length, date) in cursor:
        results["matches"].append({"fasta_id":fasta_id,
                        "a":a,
                        "g":g,
                        "c":c,
                        "t":t,
                        "gc":gc,
                        "pur":pur,
                        "pyr":pyr,
                        "Length":length,
                        "date":str(date)                        
                        })
        results["match_count"] += 1

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()
