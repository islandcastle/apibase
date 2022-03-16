"""init

Revision ID: 01e5f612c5c8
Revises: 72095c663854
Create Date: 2022-03-16 22:41:24.588947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01e5f612c5c8'
down_revision = '72095c663854'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tuusrinf',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('userid', sa.String, nullable=False),
        sa.Column('passwd', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('tuusrinf')