from alembic import op
import sqlalchemy as sa


revision = 'a5ba7703efe6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('facts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submitter', sa.String(length=250), nullable=True),
    sa.Column('fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )



def downgrade():

    op.drop_table('facts')
  