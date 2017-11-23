"""add field from manufacturing or invention

Revision ID: 87f483ad57c2
Revises: d03236a0cda4
Create Date: 2017-11-07 16:28:39.672000

"""

# revision identifiers, used by Alembic.
revision = '87f483ad57c2'
down_revision = 'd03236a0cda4'

import sqlalchemy as sa

from alembic import op
from sqlalchemy.dialects import mysql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('is_from_manufacturing', sa.Boolean(), nullable=True))
    op.add_column('item', sa.Column('is_from_reaction', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'is_from_reaction')
    op.drop_column('item', 'is_from_manufacturing')
    # ### end Alembic commands ###