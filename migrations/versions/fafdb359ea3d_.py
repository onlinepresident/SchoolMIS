"""empty message

Revision ID: fafdb359ea3d
Revises: 8a419e17de34
Create Date: 2020-01-23 00:23:58.930165

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fafdb359ea3d'
down_revision = '8a419e17de34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_academic_calendar_id', table_name='academic_calendar')
    op.create_foreign_key(None, 'billing', 'academic_calendar', ['academic_calendar_id'], ['id'])
    op.create_foreign_key(None, 'billing', 'student_category', ['student_category_id'], ['id'])
    op.create_foreign_key(None, 'billing', 'student', ['student_id'], ['student_id'])
    op.drop_column('billing', 'amount')
    op.add_column('fee_category', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.drop_column('fee_category', 'fee_category_id')
    op.add_column('fee_schedule', sa.Column('id', sa.Integer(), nullable=False, auto_increment=True))
    op.add_column('fee_schedule', sa.Column('is_current', sa.Boolean(), nullable=True))
    op.add_column('fee_schedule', sa.Column('is_percent', sa.Boolean(), nullable=True))
    op.drop_column('fee_schedule', 'is_percentage')
    op.drop_column('fee_schedule', 'fee_schedule_id')
    op.drop_column('fee_schedule', 'is_active')
    op.add_column('fee_schedule_detail', sa.Column('id', sa.Integer(), nullable=False, auto_increment=True))
    op.add_column('fee_schedule_detail', sa.Column('update_date', sa.DateTime(), nullable=True))
    op.add_column('fee_schedule_detail', sa.Column('update_user', sa.String(length=16), nullable=True))
    op.create_foreign_key(None, 'fee_schedule_detail', 'fee_schedule', ['fee_schedule_id'], ['id'])
    op.drop_column('fee_schedule_detail', 'fsd_id')
    op.drop_column('fee_schedule_detail', 'student_category_id')
    op.add_column('receipt', sa.Column('insert_date', sa.DateTime(), nullable=True))
    op.add_column('receipt', sa.Column('insert_user', sa.String(length=16), nullable=True))
    op.add_column('receipt', sa.Column('is_current', sa.Boolean(), nullable=True))
    op.add_column('receipt', sa.Column('tran_date', sa.DateTime(), nullable=True))
    op.add_column('receipt', sa.Column('tran_desc', sa.String(length=128), nullable=True))
    op.add_column('receipt', sa.Column('update_date', sa.DateTime(), nullable=True))
    op.add_column('receipt', sa.Column('update_user', sa.String(length=16), nullable=True))
    op.create_foreign_key(None, 'receipt', 'receipt_source', ['receipt_source_id'], ['id'])
    op.create_foreign_key(None, 'receipt', 'student', ['student_id'], ['student_id'])
    op.drop_column('receipt', 'insertuser')
    op.drop_column('receipt', 'trandesc')
    op.drop_column('receipt', 'updateuser')
    op.drop_column('receipt', 'academic_calendar_id')
    op.drop_column('receipt', 'trandate')
    op.drop_column('receipt', 'insertdate')
    op.drop_column('receipt', 'updatedate')
    op.add_column('receipt_source', sa.Column('id', sa.Integer(), nullable=False, auto_increment=True))
    op.create_unique_constraint(None, 'receipt_source', ['source'])
    op.drop_column('receipt_source', 'receipt_source_id')
    op.add_column('student', sa.Column('p_mobile1', sa.String(length=16), nullable=True))
    op.add_column('student', sa.Column('student_id', sa.String(length=16), nullable=False))
    op.create_index(op.f('ix_student_student_id'), 'student', ['student_id'], unique=False)
    op.create_unique_constraint(None, 'student', ['p_email'])
    op.drop_column('student', 'class')
    op.drop_column('student', 'Student_id')
    op.drop_column('student', 'p_mobile')
    op.drop_column('student', 'billing_id')
    op.drop_column('student', 'school')
    op.add_column('student_category', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.create_unique_constraint(None, 'student_category', ['description'])
    op.drop_column('student_category', 'student_category_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student_category', sa.Column('student_category_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'student_category', type_='unique')
    op.drop_column('student_category', 'id')
    op.add_column('student', sa.Column('school', mysql.CHAR(length=3), nullable=True))
    op.add_column('student', sa.Column('billing_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('student', sa.Column('p_mobile', mysql.VARCHAR(length=16), nullable=True))
    op.add_column('student', sa.Column('Student_id', mysql.VARCHAR(length=16), nullable=False))
    op.add_column('student', sa.Column('class', mysql.VARCHAR(length=3), nullable=True))
    op.drop_constraint(None, 'student', type_='unique')
    op.drop_index(op.f('ix_student_student_id'), table_name='student')
    op.drop_column('student', 'student_id')
    op.drop_column('student', 'p_mobile1')
    op.add_column('receipt_source', sa.Column('receipt_source_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'receipt_source', type_='unique')
    op.drop_column('receipt_source', 'id')
    op.add_column('receipt', sa.Column('updatedate', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('receipt', sa.Column('insertdate', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('receipt', sa.Column('trandate', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('receipt', sa.Column('academic_calendar_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('receipt', sa.Column('updateuser', mysql.VARCHAR(length=16), nullable=True))
    op.add_column('receipt', sa.Column('trandesc', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('receipt', sa.Column('insertuser', mysql.VARCHAR(length=16), nullable=True))
    op.drop_constraint(None, 'receipt', type_='foreignkey')
    op.drop_constraint(None, 'receipt', type_='foreignkey')
    op.drop_column('receipt', 'update_user')
    op.drop_column('receipt', 'update_date')
    op.drop_column('receipt', 'tran_desc')
    op.drop_column('receipt', 'tran_date')
    op.drop_column('receipt', 'is_current')
    op.drop_column('receipt', 'insert_user')
    op.drop_column('receipt', 'insert_date')
    op.add_column('fee_schedule_detail', sa.Column('student_category_id', mysql.TINYINT(display_width=4), autoincrement=False, nullable=True))
    op.add_column('fee_schedule_detail', sa.Column('fsd_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'fee_schedule_detail', type_='foreignkey')
    op.drop_column('fee_schedule_detail', 'update_user')
    op.drop_column('fee_schedule_detail', 'update_date')
    op.drop_column('fee_schedule_detail', 'id')
    op.add_column('fee_schedule', sa.Column('is_active', mysql.TINYINT(display_width=4), server_default=sa.text("'1'"), autoincrement=False, nullable=True))
    op.add_column('fee_schedule', sa.Column('fee_schedule_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.add_column('fee_schedule', sa.Column('is_percentage', mysql.TINYINT(display_width=4), server_default=sa.text("'0'"), autoincrement=False, nullable=True))
    op.drop_column('fee_schedule', 'is_percent')
    op.drop_column('fee_schedule', 'is_current')
    op.drop_column('fee_schedule', 'id')
    op.add_column('fee_category', sa.Column('fee_category_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_column('fee_category', 'id')
    op.add_column('billing', sa.Column('amount', mysql.DECIMAL(precision=19, scale=9), nullable=True))
    op.drop_constraint(None, 'billing', type_='foreignkey')
    op.drop_constraint(None, 'billing', type_='foreignkey')
    op.drop_constraint(None, 'billing', type_='foreignkey')
    op.create_index('ix_academic_calendar_id', 'academic_calendar', ['id'], unique=False)
    # ### end Alembic commands ###
