from flask import Flask, render_template
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

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
    cursor.execute("SELECT IName, Price_Quotation FROM item")
    data = cursor.fetchall()  # Fetch all rows
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    # Pass headers and results to the template
    # Convert data to a list of dictionaries for easy JS consumption
    data = [{"name": row[0], "price": row[1]} for row in data]
    return render_template('home.html', data=data)

@app.route('/testing')
def test():
    return render_template('test.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Xử lý đăng nhập ở đây
        email = request.form['email']
        password = request.form['password']

        # Kiểm tra thông tin đăng nhập (ví dụ với cơ sở dữ liệu)
        # Ở đây tạm thời kiểm tra email và password đơn giản
        if email == 'test@example.com' and password == '123':
            return redirect(url_for('home_after_signin'))
        else:
            return "Invalid login. Please try again!"

    return render_template('signin.html')
@app.route('/home_after_signin')
def home_after_signin():
    return render_template('home_after_signin.html')
@app.route('/logout')
def logout():
    # Chỉ cần chuyển hướng về trang đăng nhập
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
