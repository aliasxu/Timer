#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask_wtf import  FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class TimeForm(FlaskForm):
    timer = StringField(u'请输入时间',validators=[DataRequired()])
    submit = SubmitField(u'开始计时')
