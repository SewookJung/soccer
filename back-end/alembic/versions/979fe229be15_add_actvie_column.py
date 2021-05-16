"""Add actvie column

Revision ID: 979fe229be15
Revises: 692c662d6339
Create Date: 2021-05-14 19:17:00.480125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "979fe229be15"
down_revision = "692c662d6339"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("is_active", sa.Boolean, default=True))


def downgrade():
    op.drop_column("uesrs", "is_active")
