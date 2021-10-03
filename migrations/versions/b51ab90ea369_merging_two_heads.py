"""merging two heads

Revision ID: b51ab90ea369
Revises: 045b49dd5ce2, 4c99acf9d3d9
Create Date: 2021-10-03 10:16:56.591839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b51ab90ea369'
down_revision = ('045b49dd5ce2', '4c99acf9d3d9')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
