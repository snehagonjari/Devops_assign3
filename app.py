from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Basic validation
        if not username or not email or not password:
            flash("All fields are required!", "error")
            return redirect(url_for('register'))

        # Save data to database.txt file
        try:
            with open('database.txt', 'a') as db:
                db.write(f"Username: {username}, Email: {email}, Password: {password}\n")
        except Exception as e:
            flash(f"An error occurred: {e}", "error")
            return redirect(url_for('register'))

        flash("Registration successful!", "success")
        return redirect(url_for('register'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
