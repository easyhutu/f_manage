"""empty message

Revision ID: 98335482f277
Revises: 0e00d1e14f46
Create Date: 2018-05-15 22:58:48.606169

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '98335482f277'
down_revision = '0e00d1e14f46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('s_user', sa.Column('assess_key', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('s_user', 'assess_key')
    # ### end Alembic commands ###