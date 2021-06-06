"""ADD active column

Revision ID: 0acc2521ee4b
Revises: 6de1d1cf6261
Create Date: 2021-05-30 16:13:05.403703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0acc2521ee4b"
down_revision = "6de1d1cf6261"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("is_active", sa.Boolean, default=True))


def downgrade():
    op.drop_column("uesrs", "is_active")
