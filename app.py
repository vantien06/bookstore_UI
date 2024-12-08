from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': '47.130.34.77',
    'user': 'tien',
    'password': 'vantien123@',
    'database': 'bookwebdbs'
}

@app.route('/')
def home():
    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    # Execute the query
    cursor.execute("SELECT * FROM Customer")
    results = cursor.fetchall()  # Fetch all rows

    # Get column names from the cursor
    headers = [desc[0] for desc in cursor.description]
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    # Pass headers and results to the template
    return render_template('home.html', headers=headers, data=results)

if __name__ == '__main__':
    app.run(debug=True)
