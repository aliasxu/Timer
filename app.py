#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import re

from flask import Flask,render_template,url_for,redirect,flash,request
from forms import TimeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Please do not guess'

@app.route('/')
def index():
    return redirect(url_for('timer',num=25*60))

@app.route('/<int:num>s')
@app.route('/<int:num>')
def timer(num):
    return render_template('index.html',num=num)


@app.route('/custom',methods=['GET','POST'])
def custom():
    form = TimeForm()
    if form.validate_on_submit():
        times = form.timer.data
        if times[-1] not in 'smh':
            flash(u'请输入正确的格式，如20s,15m,2h')
            return redirect(url_for('timer',form=form))
        else:
            type={'s':'seconds','m':'minutes','h':'hours'}
            return redirect(url_for(type[times[-1]],num=int(times[:-1])))
    return redirect(url_for('index',form=form))

