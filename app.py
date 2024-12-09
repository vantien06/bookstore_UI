from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for using session

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
    cursor.execute("SELECT IName, Price_Quotation FROM item ORDER BY Brand DESC")
    data = cursor.fetchall()  # Fetch all rows
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    # Pass headers and results to the template
    # Convert data to a list of dictionaries for easy JS consumption
    data = [{"name": row[0], "price": row[1]} for row in data]
    return render_template('home.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    ID = session.get('username', None)
    if ID is None:  # Check if the user is not logged in
        return redirect(url_for('login'))  # Redirect to the login page

    # Connect to the databasef
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    query = "SELECT * FROM Customer WHERE Customer_ID = %s"
    cursor.execute(query, (ID,))  # Pass ID as a parameter to avoid SQL injection
    data = cursor.fetchall()  # Fetch all rowsows

    query = "SELECT MRank FROM membership WHERE Customer_ID = %s"
    cursor.execute(query, (ID,))  # Pass ID as a parameter to avoid SQL injection
    rank = cursor.fetchall()  # Fetch all rowsows

    query = "SELECT Email FROM CustomerEmail     WHERE Customer_ID = %s"
    cursor.execute(query, (ID,))  # Pass ID as a parameter to avoid SQL injection
    email = cursor.fetchall()  # Fetch all rowsows
    
    
    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Check if a rank was found and assign the first one (assuming only one rank per customer)
    rank_value = rank[0][0] if rank else None  # If there's no rank, set it to None

    email_value = email[0][0] if email else None  # If there's no rank, set it to None

    data = [{"Customer_ID": row[0], "CName": row[1], "Address": row[2], "Phone": row[3], "Gender": row[4], "Rank": rank_value, "Email": email_value} for row in data]

    
    return render_template('profile.html', data = data)

@app.route('/signin', methods=['GET', 'POST'])
def signin():

    # Connect to the databasef
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    # Execute the query to fetch item names and prices
    cursor.execute("SELECT Customer_ID FROM Customer")
    data = cursor.fetchall()  # Fetch all rows
    customer_ids = [item[0] for item in data]
    
    # Close the cursor and connection
    cursor.close()
    connection.close()


    if request.method == 'POST':
        # Xử lý đăng nhập ở đây
        username = request.form['username']
        password = request.form['password']

        # Kiểm tra thông tin đăng nhập (ví dụ với cơ sở dữ liệu)
        # Ở đây tạm thời kiểm tra email và password đơn giản
        if username in customer_ids:
            session['username'] = username
            return redirect(url_for('home_login'))
        else:
            return "Invalid login. Please try again!"

    return render_template('signin.html')


@app.route('/home_login')
def home_login():

    # Connect to the databasef
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    # Execute the query to fetch item names and prices
    cursor.execute("SELECT IName, Price_Quotation FROM item ORDER BY Brand DESC")
    data = cursor.fetchall()  # Fetch all rows
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    # Pass headers and results to the template
    # Convert data to a list of dictionaries for easy JS consumption
    data = [{"name": row[0], "price": row[1]} for row in data]
    return render_template('home_login.html', data=data)


@app.route('/logout')
def logout():
    # Chỉ cần chuyển hướng về trang đăng nhập
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    # Chỉ cần chuyển hướng về trang đăng nhập
    return render_template('cart.html')

@app.route('/view_detail')
def view_detail():
    image_url = request.args.get('image_url')
    # Now you can use the image_url in your template or for processing

    # Connect to the databasef
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM item ORDER BY Brand DESC;")  # Pass ID as a parameter to avoid SQL injection
    data = cursor.fetchall()  # Fetch all rowsows

    # Close the cursor and connection
    cursor.close()
    connection.close()


    data = [{"Item_ID": row[0], "IName": row[1], "Brand": row[2], "Material": row[3], "Manufacturer": row[4], "Price_Quotation": row[5], "Instock_Quantity": row[6]} for row in data]

    print("Image URL: ", image_url )
    # Chỉ cần chuyển hướng về trang đăng nhập
    return render_template('view_detail.html', data = data, image_url = image_url)






if __name__ == '__main__':
    app.run(debug=True, port = 5000)
