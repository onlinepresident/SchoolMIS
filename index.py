from app import app,db
from app.main.models import User, Student, Billing, Academic_calendar, Receipt

@app.shell_context_processor
def make_shell_context():
    return {'db':db
                , 'User':User
                ,'Student':Student
                , 'Billing':Billing
                ,'Academic_calendar':Academic_calendar
                ,'Receipt':Receipt}
