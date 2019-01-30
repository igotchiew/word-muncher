"""new fields in user model

Revision ID: 158e9d34ff35
Revises: d3517355008d
Create Date: 2019-01-29 17:13:54.718070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '158e9d34ff35'
down_revision = 'd3517355008d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
