from wtforms import Form, BooleanField, TextField, PasswordField, validators, StringField
# http://flask.pocoo.org/docs/patterns/wtforms/
# http://wtforms.readthedocs.org/en/latest/forms.html
#https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

class Report(Form):
     a_firstname = StringField(u'First Name', validators=[validators.input_required()])
     a_lastname = StringField(u'Last Name', validators=[validators.input_required()])
     a_Email = StringField(u'Email', validators=[validators.input_required()])
     a_Mobile = StringField(u'Mobile', validators=[validators.optional()])
     b_firstname = StringField(u'First Name', validators=[validators.input_required()])
     b_lastname = StringField(u'Last Name', validators=[validators.input_required()])
     b_place = StringField(u'Place', validators=[validators.input_required()])
     b_description = StringField(u'Description', validators=[validators.input_required()])
#     age = IntegerField(u'Age')

#    def validate_age(form, field):
#         if field.data < 13:
#            raise ValidationError("We're sorry, you must be 13 or older to register")

#    def insert_db(request):
#        if request.POST and Form.validate(self)
#            form.populate_obj(user)
#            user.save()
#        return redirect('/report')

#return render_to_response('report.html', form=form)

#    def edit_article(request):
#        article = Article.get(...)
#        form = MyForm(request.POST, article)

# when validation fail, return the page with its original value
# return render('edit.html', form=form, article=article)