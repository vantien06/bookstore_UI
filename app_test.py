from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Xử lý đăng nhập ở đây
        email = request.form['email']
        password = request.form['password']

        # Kiểm tra thông tin đăng nhập (ví dụ với cơ sở dữ liệu)
        if email == 'test@example.com' and password == 'password123':
            return redirect(url_for('home'))
        else:
            return "Invalid login. Please try again!"

    return render_template('signin.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
