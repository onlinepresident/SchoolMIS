from app import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#from app import login

class User(UserMixin, db.Model):
    __tablename__='user'

    id              = db.Column(db.Integer, primary_key = True)
    username        = db.Column(db.String(16), index= True, unique=True)
    email           = db.Column (db.String(64), index=True, unique = True)
    password_hash   = db.Column(db.String(128))
    insert_date     = db.Column(db.DateTime, default = datetime.utcnow)
    is_admin        = db.Column(db.Boolean, default = False)

    def set_password(self,password):
        self.password_hash= generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Academic_calendar(db.Model):
    __tablename__='academic_calendar'
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description     = db.Column(db.String(128), unique=True)
    start_date      = db.Column(db.DateTime,default=datetime.utcnow)
    end_date        = db.Column(db.DateTime,default = datetime.utcnow)
    academic_year   = db.Column(db.Integer)
    insert_date     = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    insert_user     = db.Column(db.String(16), default = 'system')
    update_user     = db.Column(db.String(16), default = 'system' )
    update_date     = db.Column(db.DateTime, index=True,default = datetime.utcnow)
    is_active      = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<academic_calendar {}>'.format(self.description)

class Student_category(db.Model):
    __tablename__='student_category'

    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description     = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return '<student_category {}>'.format(self.description)

class Student(db.Model):
    __tablename__='student'

    student_id      = db.Column(db.String(16),  primary_key=True, index=True)
    fname           = db.Column(db.String(64))
    sname           = db.Column(db.String(64))
    oname           = db.Column(db.String(64))
    gender          = db.Column(db.String(1))
    s_type          = db.Column(db.String(10))
    birth_date      = db.Column(db.DateTime, default = datetime.utcnow)
    level           = db.Column(db.String(16))
    school          = db.Column(db.String(3))
    s_class         = db.Column(db.String(1))
    activity_group  = db.Column(db.String(4))
    admission_year  = db.Column(db.Integer)
    parent_id       = db.Column(db.String(16))
    p_name          = db.Column(db.String(64))
    p_pno           = db.Column(db.String(32))
    p_email         = db.Column(db.String(64))
    p_mobile1       = db.Column(db.String(16))
    p_mobile2       = db.Column(db.String(16))
    p_mobile3       = db.Column(db.String(16))
    p_address       = db.Column(db.String(128))
    is_active       = db.Column(db.Boolean, default = True)
    is_fresher      = db.Column(db.Boolean, default = False)
    is_stopped      = db.Column(db.Boolean,default = False)
    is_staff        = db.Column(db.Boolean, default=False)
    insert_date     = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    insert_user     = db.Column(db.String(16), default ='system')
    update_user     = db.Column(db.String(16),default = 'system')
    update_date      = db.Column(db.DateTime, index=True,default = datetime.utcnow)

    bill            = db.relationship("Billing", backref="student", lazy='dynamic')

    def __repr__(self):
        return '<student> {} >'.format(self.sname +', ' + self.fname + ' ' + self.oname )

class Billing(db.Model):
    __tablename__='billing'

    billing_id              = db.Column(db.Integer, primary_key = True, autoincrement= True)
    student_id              = db.Column(db.String(16), db.ForeignKey('student.student_id'))
    academic_calendar_id    = db.Column(db.Integer, db.ForeignKey('academic_calendar.id'))
    amount                  = db.Column(db.Float(19,9), default = 0, nullable=False)
    insert_date             = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    insert_user             = db.Column(db.String(16), nullable=False, default = 'system')
    update_user             = db.Column(db.String(16), nullable=False, default = 'system')
    update_date             = db.Column(db.DateTime, index=True,default = datetime.utcnow)
    is_active               = db.Column(db.Boolean, default = True)

class fee_category(db.Model):
    __tablename__='fee_category'

    id              = db.Column(db.Integer, primary_key = True, autoincrement= True)
    name            = db.Column(db.String(64))
    description     = db.Column(db.String(128))

class Fee_schedule(db.Model):
    __tablename__='fee_schedule'

    id              = db.Column(db.Integer, primary_key = True, autoincrement= True)
    item            = db.Column(db.String(128))
    amount          = db.Column(db.Float, default = 0)
    is_percent      = db.Column(db.Boolean, default= True)
    is_active      = db.Column(db.Boolean, default = True)

class Fee_schedule_detail(db.Model):
    __tablename__='fee_schedule_detail'

    id                  = db.Column(db.Integer, primary_key = True, autoincrement= True)
    fee_schedule_id     = db.Column(db.Integer, db.ForeignKey('fee_schedule.id'))
    is_fresher          = db.Column(db.Boolean, default = False)
    is_staff            = db.Column(db.Boolean, default = True)
    school              = db.Column(db.String(16))
    amount              = db.Column(db.Float, default = 0, nullable=False)
    insert_date         = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    insert_user         = db.Column(db.String(16), default = 'system')
    update_user         = db.Column(db.String(16), default = 'system')
    update_date         = db.Column(db.DateTime, index=True,default = datetime.utcnow)
    is_active          = db.Column(db.Boolean, default = True)

class Receipt_source(db.Model):
    __tablename__='receipt_source'

    id              = db.Column(db.Integer, primary_key = True, autoincrement= True)
    source          = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Receipt_Source {}>'.format(self.source)

class Receipt(db.Model):
    __tablename__='receipt'

    receipt_id          = db.Column(db.Integer, primary_key = True, autoincrement= True)
    student_id          = db.Column(db.String(16), db.ForeignKey('student.student_id'))
    tran_desc           = db.Column(db.String(128), nullable=False)
    amount              = db.Column(db.Float, nullable=False)
    currency            = db.Column(db.String(3), nullable=False)
    tran_date           = db.Column(db.DateTime, default = datetime.utcnow)
    receipt_source_id   = db.Column(db.Integer, db.ForeignKey('receipt_source.id'))
    insert_date         = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    insert_user         = db.Column(db.String(16), nullable=False, default = 'system')
    update_user         = db.Column(db.String(16), nullable=False, default = 'system')
    update_date         = db.Column(db.DateTime, index=True,default = datetime.utcnow)
    is_active           = db.Column(db.Boolean, default = True)

    def __repr__(self):
        return '<Receipt {}>'.format(receipt.tran_desc)
