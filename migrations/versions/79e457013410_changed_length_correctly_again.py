"""changed length correctly again

Revision ID: 79e457013410
Revises: db8fdc76e312
Create Date: 2023-12-24 18:04:52.527079

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '79e457013410'
down_revision = 'db8fdc76e312'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.String(length=30),
               existing_nullable=True)
        batch_op.alter_column('rotation',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.String(length=30),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.alter_column('rotation',
               existing_type=sa.String(length=30),
               type_=mysql.VARCHAR(length=10),
               existing_nullable=False)
        batch_op.alter_column('status',
               existing_type=sa.String(length=30),
               type_=mysql.VARCHAR(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###
