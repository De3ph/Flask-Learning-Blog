"""empty message

Revision ID: 045b49dd5ce2
Revises: 5bef2eebc9a7
Create Date: 2021-08-20 15:28:17.450226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '045b49dd5ce2'
down_revision = '5bef2eebc9a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['title'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
