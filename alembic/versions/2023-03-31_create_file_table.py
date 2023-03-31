"""create file table

Revision ID: 7a2f3f138e7d
Revises: 890c17256c53
Create Date: 2023-03-31 18:41:03.810497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a2f3f138e7d'
down_revision = '890c17256c53'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stored_file',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('content', sa.LargeBinary(), nullable=False),
    sa.Column('name', sa.String(length=35), nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('is_private', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stored_file_path'), 'stored_file', ['path'], unique=True)
    op.create_index(op.f('ix_stored_file_user_id'), 'stored_file', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stored_file_user_id'), table_name='stored_file')
    op.drop_index(op.f('ix_stored_file_path'), table_name='stored_file')
    op.drop_table('stored_file')
    # ### end Alembic commands ###