"""init

Revision ID: 692c662d6339
Revises: 
Create Date: 2021-05-14 18:57:13.654004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "692c662d6339"
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
