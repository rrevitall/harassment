from wtforms import Form, BooleanField, TextField, PasswordField, validators, StringField
# http://flask.pocoo.org/docs/patterns/wtforms/
# http://wtforms.readthedocs.org/en/latest/forms.html
#https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

class Report(Form): #validators may need to be lowercase methods
     a_firstname = StringField(u'First Name', validators=[validators.InputRequired()])
     a_lastname = StringField(u'Last Name', validators=[validators.InputRequired()])
     a_Email = StringField(u'Email', validators=[validators.Email()])
     a_Mobile = StringField(u'Mobile', validators=[validators.Optional()])
     b_firstname = StringField(u'First Name', validators=[validators.InputRequired()])
     b_lastname = StringField(u'Last Name', validators=[validators.InputRequired()])
     b_place = StringField(u'Place', validators=[validators.InputRequired()])
     b_description = StringField(u'Description', validators=[validators.InputRequired()])
#     age = IntegerField(u'Age')

#    def validate_age(form, field):
#         if field.data < 13:
#            raise ValidationError("We're sorry, you must be 13 or older to register")

   def insert_db(request):
       if request.POST and Form.validate(self)
           form.populate_obj(user)
           user.save()
       return redirect('/report')

# return render_to_response('report.html', form=form)

#    def edit_article(request):
#        article = Article.get(...)
#        form = MyForm(request.POST, article)

# when validation fail, return the page with its original value
# return render('edit.html', form=form, article=article)