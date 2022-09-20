"""First commit

Revision ID: 5828efd7eddf
Revises: 10303531ffe7
Create Date: 2022-09-19 22:42:49.192860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5828efd7eddf'
down_revision = '10303531ffe7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('longitude', sa.String(length=200), nullable=False),
    sa.Column('latitude', sa.String(length=200), nullable=False),
    sa.Column('address', sa.JSON(), nullable=False),
    sa.Column('zoom', sa.Integer(), nullable=True),
    sa.Column('quartier', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='uc_name_type')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email', name='uc_email')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['type_id'], ['type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='uc_name_category')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('payment_method', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('phone_number', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', name='uc_user_id')
    )
    op.create_table('salon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.Column('opening_hours', sa.JSON(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='uc_name_salon')
    )
    op.create_table('client_rate',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('average', sa.String(length=20), nullable=False),
    sa.Column('comment', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('client_id', name='uc_client_id')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('salon_id', sa.Integer(), nullable=False),
    sa.Column('is_manager', sa.Boolean(), server_default='False', nullable=False),
    sa.ForeignKeyConstraint(['salon_id'], ['salon.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('salon_id', sa.Integer(), nullable=False),
    sa.Column('file_url', sa.String(length=200), nullable=False),
    sa.Column('is_main', sa.Boolean(), server_default='False', nullable=False),
    sa.ForeignKeyConstraint(['salon_id'], ['salon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prestation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('duration', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='uc_name_prestation')
    )
    op.create_table('salon_rate',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('salon_id', sa.Integer(), nullable=False),
    sa.Column('average', sa.String(length=20), nullable=False),
    sa.Column('comment', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['salon_id'], ['salon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('salon_id', sa.Integer(), nullable=False),
    sa.Column('prestation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['prestation_id'], ['prestation.id'], ),
    sa.ForeignKeyConstraint(['salon_id'], ['salon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    op.drop_table('salon_rate')
    op.drop_table('prestation')
    op.drop_table('image')
    op.drop_table('employee')
    op.drop_table('client_rate')
    op.drop_table('salon')
    op.drop_table('client')
    op.drop_table('category')
    op.drop_table('user')
    op.drop_table('type')
    op.drop_table('address')
    # ### end Alembic commands ###
