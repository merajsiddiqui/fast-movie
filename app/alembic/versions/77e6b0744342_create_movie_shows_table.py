"""create_movie_shows_table

Revision ID: 77e6b0744342
Revises: 67ad70520f35
Create Date: 2021-04-06 18:30:54.028580

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '77e6b0744342'
down_revision = '67ad70520f35'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'movie_shows',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('theater_id', sa.Integer),
        sa.Column('movie_id', sa.Integer),
        sa.Column('show_time', sa.String(50), nullable=False),
        sa.Column('hall_name', sa.String(50), nullable=False),
        sa.Column('ticket_cost', sa.Float, default=0.0),
        sa.Column('capacity', sa.Integer, default=10),
        sa.Column('is_live', sa.Boolean, default=True),
    )


def downgrade():
    op.drop_table('movie_shows')
