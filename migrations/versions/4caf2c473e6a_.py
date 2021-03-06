"""empty message

Revision ID: 4caf2c473e6a
Revises: 20b836df74cc
Create Date: 2018-07-23 11:48:11.105622

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '4caf2c473e6a'
down_revision = '20b836df74cc'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('facebook_login_hash', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'facebook_login_hash')
    # ### end Alembic commands ###
