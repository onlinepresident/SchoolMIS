"""empty message

Revision ID: a8665336cfa1
Revises: bcea2dc55eb6
Create Date: 2020-01-24 07:09:23.577482

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a8665336cfa1'
down_revision = 'bcea2dc55eb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('student', 'admission_year',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('student', 'admission_year',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    # ### end Alembic commands ###
