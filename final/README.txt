* ABOUT *

Web page for entering in fasta entries for a database based on properties of the sequence.

Source code:
http://bfx.eng.jhu.edu/jnguye36/final_project/final.tar.gz

Active demo:
http://bfx.eng.jhu.edu/jnguye36/final/search.html

* Requirements *
Should be none for the web based user.
In order to deploy, it requires Python3 and a MySQL database configured. 
Credentials can be entered into the .cgi scripts
Storage is required for the SQL database, but memory usage should be low.

* Detailed Usage *

Fasta Entry
1. Enter in Accession number to be used as an id
2. Enter in sequence corresponding to id

Fasta Search
1. Enter in term to search by
	a. Accession will search using a LIKE %[TERM]% syntax in SQL
	b. All other fields are based in percentages, and will be given a range of +/- 5%.
2. Select which property to search by.

Output
1. A table will appear that gives
	a. Nucleotide counts
	b. Percentages of GC, PUR, and PYR
	c. Length
	d. Date entered into database