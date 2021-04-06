"""create_bookings_table

Revision ID: 456c5da0a9ac
Revises: 77e6b0744342
Create Date: 2021-04-06 18:31:07.018835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '456c5da0a9ac'
down_revision = '77e6b0744342'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'bookings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('show_id', sa.Integer),
        sa.Column('ticket_code', sa.String(50), nullable=False),
        sa.Column('amount_paid', sa.Float, default=0.0),
        sa.Column('deleted', sa.Boolean, default=False),
    )


def downgrade():
    op.drop_table('bookings')