"""add implants in prefs

Revision ID: 02bf73d552c2
Revises: 86d4d399a174
Create Date: 2017-03-10 22:22:29.104000

"""

# revision identifiers, used by Alembic.
revision = '02bf73d552c2'
down_revision = '86d4d399a174'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_preference', sa.Column('invention_copy_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False))
    op.add_column('user_preference', sa.Column('research_copy_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False))
    op.add_column('user_preference', sa.Column('research_me_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False))
    op.add_column('user_preference', sa.Column('research_te_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_preference', 'research_te_implant')
    op.drop_column('user_preference', 'research_me_implant')
    op.drop_column('user_preference', 'research_copy_implant')
    op.drop_column('user_preference', 'invention_copy_implant')
    # ### end Alembic commands ###