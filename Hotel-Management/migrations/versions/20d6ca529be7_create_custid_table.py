"""create custid table

Revision ID: 20d6ca529be7
Revises: 
Create Date: 2019-06-14 12:52:28.297030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20d6ca529be7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('room', sa.Column('cust_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'room', 'customer', ['cust_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'room', type_='foreignkey')
    op.drop_column('room', 'cust_id')
    # ### end Alembic commands ###
