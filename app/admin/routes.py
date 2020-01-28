from flask import Blueprint
from flask import render_template
from flask_login import login_required


blue = Blueprint('admin', __name__, template_folder = 'templates', url_prefix='/admin')
@blue.route('/', methods = ['GET', 'POST'])
@login_required
def index():
    return render_template('admin/index.html')
    #return 'dashboard not working'

# @blue.route('/logout', methods = ['GET', 'POST'])
# def logout():
#     logout_user()
#     return redirect(url_for('login.index'))
