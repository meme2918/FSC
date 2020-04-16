SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_BINDS = {
    'my_sql1': 'mysql://root:Saleh2009$@localhost/Posts',
    #'my_sql2': 'mysql://root:password@externalserver.domain.com/quickhowto2'
}