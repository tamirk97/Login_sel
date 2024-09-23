from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used to secure the session

# Dummy users database
users = {
    "admin": "password123",
    "user": "pass123"
}

@app.route('/')
def home():
    if 'username' in session:
        return f"Hello, {session['username']}! <br><a href='/logout'>Logout</a>"
    return "You are not logged in! <br><a href='/login'>Login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate credentials
        if username in users and users[username] == password:
            session['username'] = username  # Store username in session
            flash("Logged in successfully!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials, try again!", "danger")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out!", "info")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
