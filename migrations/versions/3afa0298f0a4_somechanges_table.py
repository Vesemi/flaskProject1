"""somechanges table

Revision ID: 3afa0298f0a4
Revises: 68ee37129559
Create Date: 2022-12-27 01:30:27.165696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3afa0298f0a4'
down_revision = '68ee37129559'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=140), nullable=True))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=140), nullable=True))
        batch_op.drop_column('title')

    # ### end Alembic commands ###