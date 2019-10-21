"""empty message

Revision ID: 0dcebd374a24
Revises: 8950168611a2
Create Date: 2018-03-23 09:56:49.921525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dcebd374a24'
down_revision = '8950168611a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('password', sa.String(length=128), nullable=True))
    op.create_unique_constraint(None, 'users', ['phoneNumber'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('admins', 'password')
    # ### end Alembic commands ###
