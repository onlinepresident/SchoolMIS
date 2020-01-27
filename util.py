
#Clear data in all tables in ur database
def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print 'Clear table %s' % table
        session.execute(table.delete()) #db.drop_all()  to drop all the tables
    session.commit()
