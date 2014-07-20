from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from ClassForm import Report

# import MySQLdb

app = Flask(__name__)
# Open database connection
#db = MySQLdb.connect("localhost","team","team","team" )
#db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# sql = " insert into harassment_list ( applier_firstn, applier_lastn, applier_mobile, \
# applier_email, harassment_firstn, harassment_lastn,  harassment_place)  \
# values (null, null, null, null, null, null, null ) " %  \

engine = create_engine('mysql://team:team@localhost/team',convert_unicode=True)
#engine = create_engine('mysql://team:team@localhost/team',convert_unicode=True)
#engine = create_engine('mysql:////var/lib/mysql/team.db', convert_unicode=True)
#engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
# http://dev.mysql.com/doc/refman/5.6/en/option-files.html
# http://en.opensuse.org/SDB:MySQL_installation
  
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Form_Validate', methods=['POST'])
def form_validate():
    report=Report(request.POST)
    #report.save()
    return redirect('/report')

#  engine.execute('select * from users where id = :1', [1]).first()
#(1, u'admin', u'admin@localhost')

if __name__ == '__main__':
  app.run(debug=True)

