"""Add nick name of user table

Revision ID: 8ac78eac1c7e
Revises: 0acc2521ee4b
Create Date: 2021-06-06 14:46:34.638903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ac78eac1c7e'
down_revision = '0acc2521ee4b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("nickname", sa.String))


def downgrade():
    op.drop_column("uesrs", "nickname")
