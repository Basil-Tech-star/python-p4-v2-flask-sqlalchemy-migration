"""rename address

Revision ID: c5ed5a9c4703
Revises: 01415f306bfb
Create Date: 2025-01-25 05:51:02.883155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5ed5a9c4703'
down_revision = '01415f306bfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('departments', sa.Column('location', sa.String(), nullable=False))
    # op.drop_column('departments', 'address')
    op.alter_column('departments', 'address', new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    # op.drop_column('departments', 'location')
    op.alter_column('departments', 'location', new_column_name = 'address')
    # ### end Alembic commands ###
