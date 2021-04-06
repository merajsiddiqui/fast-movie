"""create_movies_table

Revision ID: 67ad70520f35
Revises: 2fdecc3d0582
Create Date: 2021-04-06 18:29:56.047338

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '67ad70520f35'
down_revision = '2fdecc3d0582'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'movies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('movies')
