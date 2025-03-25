"""empty message

Revision ID: a8a9c8116e3d
Revises: 
Create Date: 2025-03-11 13:06:31.242157

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# Revision identifiers
revision = 'a8a9c8116e3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # 🚀 1️⃣ Drop Foreign Key Constraints First
    op.drop_constraint('contracts_ibfk_1', 'contracts', type_='foreignkey')
    op.drop_constraint('transactions_ibfk_1', 'transactions', type_='foreignkey')
    op.drop_constraint('technician_schedule_ibfk_2', 'technician_schedule', type_='foreignkey')

    # 🚀 2️⃣ Drop Dependent Tables
    op.drop_table('technician_schedule')
    op.drop_table('maintenance_requests')
    op.drop_table('transactions')
    op.drop_table('contracts')

    # 🚀 3️⃣ Drop Main Tables
    op.drop_table('apartments')
    op.drop_table('users')

    # 🚀 4️⃣ Create Updated Users Table
    op.create_table('users',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('full_name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('phone_number', sa.String(20), nullable=False),
        sa.Column('role', sa.Enum('Owner', 'Administrator', 'Buyer/Tenant', 'Technician', name='user_roles'), nullable=False),
        sa.Column('job', sa.String(255), nullable=True),
        sa.Column('facebook_link', sa.String(255), nullable=True),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('is_verified', sa.Boolean, default=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'))
    )

    # 🚀 5️⃣ Create Updated Apartments Table
    op.create_table('apartments',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('owner_id', sa.BigInteger, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('location', sa.String(255), nullable=False),
        sa.Column('unit_number', sa.String(50), nullable=False),
        sa.Column('area', sa.Numeric(10, 2), nullable=False),
        sa.Column('number_of_rooms', sa.Integer, nullable=False),
        sa.Column('type', sa.Enum('For Sale', 'For Rent', name='apartment_type'), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('photos', sa.JSON, nullable=True),
        sa.Column('parking_availability', sa.Boolean, nullable=True),
        sa.Column('video', sa.Text, nullable=True),  # ✅ Fixed: Added Video Column
        sa.Column('map_location', sa.Text, nullable=True),  # ✅ Fixed: Added Map Location Column
        sa.Column('status', sa.Enum('Available', 'Sold', 'Rented', name='apartment_status'), default='Available'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'))
    )

    # 🚀 6️⃣ Recreate Transactions Table
    op.create_table('transactions',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('apartment_id', sa.BigInteger, sa.ForeignKey('apartments.id')),
        sa.Column('user_id', sa.BigInteger, sa.ForeignKey('users.id')),
        sa.Column('amount', sa.Numeric(12, 2), nullable=False),
        sa.Column('transaction_type', sa.Enum('Rent', 'Sale', 'Maintenance', name='transaction_types'), nullable=False),
        sa.Column('status', sa.Enum('Pending', 'Completed', 'Overdue', name='transaction_status'), nullable=False),
        sa.Column('payment_method', sa.Enum('Visa', 'MasterCard', 'Cash', name='payment_methods'), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'))
    )

    # 🚀 7️⃣ Recreate Maintenance Requests Table
    op.create_table('maintenance_requests',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('apartment_id', sa.BigInteger, sa.ForeignKey('apartments.id')),
        sa.Column('user_id', sa.BigInteger, sa.ForeignKey('users.id')),
        sa.Column('technician_id', sa.BigInteger, sa.ForeignKey('users.id')),
        sa.Column('problem_type', sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('images', sa.JSON, nullable=True),
        sa.Column('status', sa.Enum('Pending', 'In Progress', 'Resolved', 'Cancelled', name='request_status'), default='Pending'),
        sa.Column('request_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('response', sa.Text, nullable=True)
    )

    # 🚀 8️⃣ Recreate Contracts Table
    op.create_table('contracts',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('apartment_id', sa.BigInteger, sa.ForeignKey('apartments.id')),
        sa.Column('user_id', sa.BigInteger, sa.ForeignKey('users.id')),
        sa.Column('contract_details', sa.Text, nullable=False),
        sa.Column('signed', sa.Boolean, default=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'))
    )

    # 🚀 9️⃣ Recreate Technician Schedule Table
    op.create_table('technician_schedule',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('technician_id', sa.BigInteger, sa.ForeignKey('users.id')),
        sa.Column('request_id', sa.BigInteger, sa.ForeignKey('maintenance_requests.id')),
        sa.Column('scheduled_date', sa.DateTime(), nullable=False),
        sa.Column('status', sa.Enum('Scheduled', 'Completed', 'Cancelled', name='schedule_status'), nullable=False),
        sa.Column('cancellation_reason', sa.Text, nullable=True)
    )


def downgrade():
    # ❌ Undo all changes in reverse order
    op.drop_table('technician_schedule')
    op.drop_table('contracts')
    op.drop_table('maintenance_requests')
    op.drop_table('transactions')
    op.drop_table('apartments')
    op.drop_table('users')
