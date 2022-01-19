"""empty message

Revision ID: 744f28a07720
Revises: 88ef3fcf5909
Create Date: 2021-10-19 19:41:13.502352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '744f28a07720'
down_revision = '88ef3fcf5909'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###