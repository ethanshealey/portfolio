from app import app, mail
from flask import render_template, flash, url_for, redirect
from app.forms import ContactForm
from flask_mail import Message

@app.route('/', methods=['GET','POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message('[ethanshealey.com] New Message!', sender=app.config['ADMINS'][0], recipients=['ethanshealey@gmail.com'])
        msg.body=render_template('msg.txt', data=form)
        msg.html=render_template('msg.html', data=form)
        mail.send(msg)
        return redirect(url_for('index'))
    return render_template('index.html', title='Portfolio | Ethan Shealey', form=form)
