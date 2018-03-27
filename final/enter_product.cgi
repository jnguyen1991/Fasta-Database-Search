#!/usr/local/bin/python3

#enters data in
#processes it, and returns back a query
#with the term entered as a search term

import cgi, json
import os
import mysql.connector
import fasta_analyze
import datetime

def main():
    print("Content-Type: application/json\n\n")
    #print("Content-Type: text/html\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('acc')
    sequence = form.getvalue('sequence')

    
    fs = fasta_analyze.fasta_summary(sequence)
    conn = mysql.connector.connect(user='jnguye36', password='J0n!7301991', host='localhost', database='jnguye36')
    cursor = conn.cursor()
    
    check_qry = """
        SELECT name
        FROM final
        WHERE name = %s
    """
    cursor.execute(check_qry, (term ,))
    check_output = []
    for i in cursor:
        check_output.append(i)
    if len(check_output) < 1:          
        insert_qry = """
              INSERT INTO final(name, a, g, c, t, gc, purine, pyrimidine, length, date)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_qry, (term, fs["A"], fs["G"], fs["C"], fs["T"], fs["GC Content"], fs["Purine"], fs["Pyrimidine"], fs["Length"], datetime.datetime.today().strftime('%Y-%m-%d')))
    
    qry = """
          SELECT name, a, g, c, t, gc, purine, pyrimidine, length, date
            FROM final
           WHERE name LIKE %s
    """
    cursor.execute(qry, ('%' + term + '%',))
  


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
