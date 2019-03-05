"""modify db

Revision ID: 3b07126a920b
Revises: 5e88a7828202
Create Date: 2018-12-26 23:57:05.937262

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3b07126a920b'
down_revision = '5e88a7828202'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'c_time')
    op.add_column('supply', sa.Column('fast_mail', sa.String(length=20), nullable=False))
    op.drop_column('supply', 'qq')
    op.drop_column('supply', 'fast_mail_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supply', sa.Column('fast_mail_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('supply', sa.Column('qq', mysql.VARCHAR(length=15), nullable=True))
    op.drop_column('supply', 'fast_mail')
    op.add_column('image', sa.Column('c_time', sa.DATE(), nullable=False))
    # ### end Alembic commands ###