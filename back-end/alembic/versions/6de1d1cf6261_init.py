"""init

Revision ID: 6de1d1cf6261
Revises: 
Create Date: 2021-05-30 15:42:24.237369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6de1d1cf6261"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("email", sa.String, unique=True),
        sa.Column("password", sa.String),
    )


def downgrade():
    op.drop_table("users")
