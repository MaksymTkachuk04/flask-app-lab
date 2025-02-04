"""add publish_date field

Revision ID: a9602119e52b
Revises: 1e45b725c51b
Create Date: 2024-11-20 19:54:03.066573

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = 'a9602119e52b'
down_revision = '1e45b725c51b'
branch_labels = None
depends_on = None

def upgrade():
    # Додавання нового стовпця без дефолтного значення
    op.add_column('posts', sa.Column('publish_date', sa.DateTime(), nullable=False))

def downgrade():
    # Видалення стовпця 'publish_date'
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('publish_date')
