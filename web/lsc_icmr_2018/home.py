import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return render_template('home/index.html')
    
@bp.route('/result', methods=('GET', 'POST'))
def result():
    if request.method == 'GET':
        time = request.form['time']
        place = request.form['place']
        obj = request.form['obj']
        action = request.form['action']

    #     if not time:
    #         error = 'Time is required'
    #     elif not place:
    #         error = 'Place is required'
    #     elif (not obj) and (not action):
    #         error = 'Object or Action is required'

    #     if error is None:
    #         pass

    #     flash(error)
    return render_template('home/result.html')
