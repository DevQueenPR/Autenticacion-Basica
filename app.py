from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Credenciales
users = {
    "admin": {"password": generate_password_hash("adminpass"), "role": "admin"},
    "user": {"password": generate_password_hash("userpass"), "role": "user"}
}

class User(UserMixin):
    def __init__(self, username, role):
        self.id = username
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    user = users.get(user_id)
    if user:
        return User(user_id, user["role"])
    return None

# Rutas 
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None  
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.get(username)
        if user and check_password_hash(user["password"], password):
            login_user(User(username, user["role"]))
            return redirect(url_for("dashboard"))
        else:
            error = "Credenciales incorrectas. Inténtalo de nuevo."

    return render_template("login.html", error=error)


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", name=current_user.id, role=current_user.role)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/users")
def list_users():
    return users

if __name__ == "__main__":
    app.run(debug=True)
