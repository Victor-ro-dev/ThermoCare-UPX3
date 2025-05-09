"""Upgrade dos campos do NursingHome

Revision ID: 2e42d26617d4
Revises: 1098d063da19
Create Date: 2025-03-26 23:12:18.725617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e42d26617d4'
down_revision: Union[str, None] = '1098d063da19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nursing_homes', sa.Column('cep', sa.String(length=9), nullable=False))
    op.add_column('nursing_homes', sa.Column('logradouro', sa.String(length=255), nullable=False))
    op.add_column('nursing_homes', sa.Column('numero', sa.String(length=10), nullable=False))
    op.add_column('nursing_homes', sa.Column('bairro', sa.String(length=100), nullable=False))
    op.add_column('nursing_homes', sa.Column('cidade', sa.String(length=100), nullable=False))
    op.add_column('nursing_homes', sa.Column('estado', sa.String(length=2), nullable=False))
    op.add_column('nursing_homes', sa.Column('complemento', sa.String(length=255), nullable=True))
    op.drop_column('nursing_homes', 'address')
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.add_column('nursing_homes', sa.Column('address', sa.VARCHAR(length=255), nullable=False))
    op.drop_column('nursing_homes', 'complemento')
    op.drop_column('nursing_homes', 'estado')
    op.drop_column('nursing_homes', 'cidade')
    op.drop_column('nursing_homes', 'bairro')
    op.drop_column('nursing_homes', 'numero')
    op.drop_column('nursing_homes', 'logradouro')
    op.drop_column('nursing_homes', 'cep')
    # ### end Alembic commands ###
