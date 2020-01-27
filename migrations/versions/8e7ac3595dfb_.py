"""empty message

Revision ID: 8e7ac3595dfb
Revises: 83fbe88761ba
Create Date: 2020-01-23 00:55:36.921456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e7ac3595dfb'
down_revision = '83fbe88761ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('academic_calendar',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('academic_year', sa.Integer(), nullable=True),
    sa.Column('insert_date', sa.DateTime(), nullable=True),
    sa.Column('insert_user', sa.String(length=16), nullable=True),
    sa.Column('update_user', sa.String(length=16), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('is_current', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    op.create_table('fee_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fee_schedule',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('item', sa.String(length=128), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('is_percent', sa.Boolean(), nullable=True),
    sa.Column('is_current', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receipt_source',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('source', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('source')
    )
    op.create_table('student',
    sa.Column('student_id', sa.String(length=16), nullable=False),
    sa.Column('fname', sa.String(length=32), nullable=True),
    sa.Column('sname', sa.String(length=32), nullable=True),
    sa.Column('oname', sa.String(length=32), nullable=True),
    sa.Column('gender', sa.String(length=1), nullable=True),
    sa.Column('s_type', sa.String(length=1), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('level', sa.String(length=16), nullable=True),
    sa.Column('activity_group', sa.String(length=1), nullable=True),
    sa.Column('admission_year', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.String(length=16), nullable=True),
    sa.Column('p_name', sa.String(length=64), nullable=True),
    sa.Column('p_pno', sa.String(length=32), nullable=True),
    sa.Column('p_email', sa.String(length=64), nullable=True),
    sa.Column('p_mobile1', sa.String(length=16), nullable=True),
    sa.Column('p_mobile2', sa.String(length=16), nullable=True),
    sa.Column('p_mobile3', sa.String(length=16), nullable=True),
    sa.Column('p_address', sa.String(length=128), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_fresher', sa.Boolean(), nullable=True),
    sa.Column('is_stopped', sa.Boolean(), nullable=True),
    sa.Column('is_staff', sa.Boolean(), nullable=True),
    sa.Column('insert_date', sa.DateTime(), nullable=True),
    sa.Column('insert_user', sa.String(length=16), nullable=True),
    sa.Column('update_user', sa.String(length=16), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('student_id'),
    sa.UniqueConstraint('p_email')
    )
    op.create_index(op.f('ix_student_student_id'), 'student', ['student_id'], unique=False)
    op.create_table('student_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=16), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('insert_date', sa.DateTime(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('billing',
    sa.Column('billing_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.String(length=16), nullable=True),
    sa.Column('student_category_id', sa.Integer(), nullable=True),
    sa.Column('academic_calendar_id', sa.Integer(), nullable=True),
    sa.Column('insert_date', sa.DateTime(), nullable=True),
    sa.Column('insert_user', sa.String(length=16), nullable=True),
    sa.Column('update_user', sa.String(length=16), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('is_current', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['academic_calendar_id'], ['academic_calendar.id'], ),
    sa.ForeignKeyConstraint(['student_category_id'], ['student_category.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('billing_id')
    )
    op.create_table('fee_schedule_detail',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fee_schedule_id', sa.Integer(), nullable=True),
    sa.Column('is_fresher', sa.Boolean(), nullable=True),
    sa.Column('is_staff', sa.Boolean(), nullable=True),
    sa.Column('school', sa.String(length=16), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('insert_date', sa.DateTime(), nullable=True),
    sa.Column('insert_user', sa.String(length=16), nullable=True),
    sa.Column('update_user', sa.String(length=16), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('is_current', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['fee_schedule_id'], ['fee_schedule.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receipt',
    sa.Column('receipt_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.String(length=16), nullable=True),
    sa.Column('tran_desc', sa.String(length=128), nullable=True),
    sa.Column('amount', sa.String(length=128), nullable=True),
    sa.Column('currency', sa.String(length=3), nullable=True),
    sa.Column('tran_date', sa.DateTime(), nullable=True),
    sa.Column('receipt_source_id', sa.Integer(), nullable=True),
    sa.Column('insert_date', sa.DateTime(), nullable=True),
    sa.Column('insert_user', sa.String(length=16), nullable=True),
    sa.Column('update_user', sa.String(length=16), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('is_current', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['receipt_source_id'], ['receipt_source.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('receipt_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('receipt')
    op.drop_table('fee_schedule_detail')
    op.drop_table('billing')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('student_category')
    op.drop_index(op.f('ix_student_student_id'), table_name='student')
    op.drop_table('student')
    op.drop_table('receipt_source')
    op.drop_table('fee_schedule')
    op.drop_table('fee_category')
    op.drop_table('academic_calendar')
    # ### end Alembic commands ###