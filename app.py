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
    # Connect to the databasef
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    # Execute the query to fetch item names and prices
    cursor.execute("SELECT IName, Price_Quotation FROM item ORDER BY RAND()")
    data = cursor.fetchall()  # Fetch all rows
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    # Pass headers and results to the template
    # Convert data to a list of dictionaries for easy JS consumption
    data = [{"name": row[0], "price": row[1]} for row in data]
    return render_template('home.html', data=data)

@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')



if __name__ == '__main__':
    app.run(debug=True)
