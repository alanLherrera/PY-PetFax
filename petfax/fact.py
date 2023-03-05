from flask import (Blueprint, render_template, request, redirect)
from . import models

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/', methods=['GET','POST'])
def index():
  if request.method == 'POST':
    submitter2 = request.form['submitter']
    fact2 = request.form['fact']

    new_fact = models.Fact(submitter=submitter2,fact=fact2)
    models.db.session.add(new_fact)
    models.db.session.commit()


    return redirect('/facts')

  results = models.Fact.query.all()
  
  return render_template('facts/index.html', facts=results)

@bp.route('/new')
def new():
  return render_template('facts/new.html')