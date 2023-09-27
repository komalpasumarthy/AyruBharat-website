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


def get_disease(symptoms):
  if symptoms is None:
    return None

  cnx = get_connector()
  cursor = cnx.cursor()

  query = "SELECT * FROM Ayurved WHERE symptoms LIKE %s LIMIT 1"
  
  cursor.execute(query, ('%'+symptoms+'%',))
  data = cursor.fetchall()
  cursor.close()
  cnx.close()
  return data



def insert_user(name, email, phone, password):
  cnx = get_connector()
  cursor = cnx.cursor()
  
  query = "INSERT INTO user VALUES (%s, %s, %s, %s)"
  
  cursor.execute(query, (name, email, phone, password) )
  cnx.commit()
  cursor.close()
  cnx.close()
  

def check_user(email, password):
  cnx = get_connector()
  cursor = cnx.cursor()
  cursor.execute("SELECT * FROM user WHERE email=%s", (email,))
  user = cursor.fetchone()
  cnx.close()
    
  if user:
      if user[3] == password:  # assuming password is stored in 4th column
          return True, True
      else:
          return True, False
  return False, False