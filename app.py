from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Pour simplifier, stockage des identifients d'utilisateur dans un dictionnaire 
users = {'utilisateur1': 'motdepasse1', 'utilisateur2': 'motdepasse2', 'utilisateur3': 'motdepasse3'}

class LoginForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')
    erase = SubmitField('Effacer')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username in users and users[username] == password:
            flash(f'Connexion réussie pour {username}!', 'success')
        else:
            flash('Échec de la connexion. Veuillez vérifier vos informations.', 'danger')

        return redirect(url_for('login'))

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
