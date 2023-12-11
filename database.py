from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'employee'
}

# Function to connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(**mysql_config)
        print(f"Connected succesfully...")
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

@app.route('/')
def index():
   return render_template('index.html')

# Route to insert employee data into MySQL
@app.route('/add_employee', methods=['POST'])
def add_employee():
    try:
        data = request.get_json()
        if data:
            conn = connect_to_database()
            if conn:
                cursor = conn.cursor()

                query = "INSERT INTO registration (EMPLOYEEID, NAME, DOB, AGE, JOININGDATE, EXPERIENCE, EMAIL,PhNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                employee_values = (
                    data['EMPLOYEEID'], data['NAME'], data['DOB'], data['AGE'], data['JOININGDATE'],
                    data['EXPERIENCE'], data['EMAIL'], data['PhNo']
                )
                cursor.execute(query, employee_values)

                conn.commit()
                cursor.close()
                conn.close()
                return jsonify({'message': 'Employee details added successfully'})
            else:
                return jsonify({'error': 'Failed to connect to the database'})
        else:
            return jsonify({'error': 'No data provided'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
