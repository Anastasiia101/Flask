"""empty message

Revision ID: 35da1b581717
Revises: bb12314c4b7f
Create Date: 2021-03-24 13:00:43.882141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35da1b581717'
down_revision = 'bb12314c4b7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('isAnswer', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answers', 'isAnswer')
    # ### end Alembic commands ###
