"""create_users_table

Revision ID: 39df24ee7dba
Revises: 
Create Date: 2021-04-06 18:29:02.854050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39df24ee7dba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('users')