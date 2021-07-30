"""init

Revision ID: e54be0271a61
Revises: 
Create Date: 2021-07-30 13:59:15.970333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e54be0271a61"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "banknote",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("variance", sa.Float(), nullable=False),
        sa.Column("skewness", sa.Float(), nullable=False),
        sa.Column("kurtosis", sa.Float(), nullable=False),
        sa.Column("entropy", sa.Float(), nullable=False),
    )


def downgrade():
    op.drop_table("banknote")
