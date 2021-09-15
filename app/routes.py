from app import app
from flask import render_template, flash, redirect, url_for  # 从flask包中导入render_template函数

from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Miguel'}
	posts = [
		{
			'author': {'username':'John'},
			'body':'Beautiful day in Portland!'
		},
		{
			'author': {'username':'Susan'},
			'body':'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for 用户 {},记不记remember_me={}'.format(form.username.data,form.remember_me.data))
		return redirect(url_for(index))
	return render_template('login.html',title='Sign In',form=form)