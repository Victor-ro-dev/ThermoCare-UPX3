"""Correção do campo nursing_home_id

Revision ID: 1098d063da19
Revises: 8ea4dc364342
Create Date: 2025-03-21 14:36:48.417494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1098d063da19'
down_revision = '8ea4dc364342'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade schema."""
    # Criar uma tabela temporária com a nova definição
    op.create_table(
        "users_temp",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=100), unique=True, nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column("nursing_home_id", sa.Integer(), sa.ForeignKey("nursing_homes.id", ondelete="SET NULL"), nullable=True),
    )

    # Copiar os dados da tabela antiga para a nova tabela
    op.execute("INSERT INTO users_temp SELECT * FROM users")

    # Remover a tabela antiga
    op.drop_table("users")

    # Renomear a tabela temporária para o nome original
    op.rename_table("users_temp", "users")


def downgrade() -> None:
    """Downgrade schema."""
    # Criar uma tabela temporária com a definição antiga
    op.create_table(
        "users_temp",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=100), unique=True, nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column("nursing_home_id", sa.Integer(), sa.ForeignKey("nursing_homes.id", ondelete="SET NULL"), nullable=False),
    )

    # Copiar os dados da tabela atual para a tabela temporária
    op.execute("INSERT INTO users_temp SELECT * FROM users")

    # Remover a tabela atual
    op.drop_table("users")

    # Renomear a tabela temporária para o nome original
    op.rename_table("users_temp", "users")
