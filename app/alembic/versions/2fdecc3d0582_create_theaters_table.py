"""create_theaters_table

Revision ID: 2fdecc3d0582
Revises: 39df24ee7dba
Create Date: 2021-04-06 18:29:47.565613

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2fdecc3d0582'
down_revision = '39df24ee7dba'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'theaters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('city', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('theaters')
