import mysql.connector

def get_connector():
  return mysql.connector.connect(
  user='sql9649376', 
  password='YPvLIfRIHG', 
  host='sql9.freesqldatabase.com', 
  database='sql9649376'
)

def get_data():
  cnx = get_connector()
  cursor = cnx.cursor()

  query = "SELECT * FROM Symptoms"
  
  cursor.execute(query)
  data = cursor.fetchall()
  cursor.close()
  cnx.close()
  return data


def get_disease(disease, symptoms):
  cnx = get_connector()
  cursor = cnx.cursor()

  query = ("SELECT * FROM Symptoms WHERE AyurTerm = %s AND symptom = %s")
  
  cursor.execute(query, (disease, symptoms))
  data = cursor.fetchall()
  cursor.close()
  cnx.close()
  return data

