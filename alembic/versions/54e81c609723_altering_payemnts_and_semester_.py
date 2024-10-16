"""Altering payemnts and semester registration

Revision ID: 54e81c609723
Revises: b6ac49a316df
Create Date: 2024-10-16 21:18:57.883774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54e81c609723'
down_revision: Union[str, None] = 'b6ac49a316df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('program_semester_student',
    sa.Column('program_id', sa.UUID(), nullable=False),
    sa.Column('semester_id', sa.UUID(), nullable=False),
    sa.Column('student_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['program_id'], ['program.program_id'], ),
    sa.ForeignKeyConstraint(['semester_id'], ['semester.semester_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('program_id', 'semester_id', 'student_id')
    )
    op.create_index(op.f('ix_program_semester_student_program_id'), 'program_semester_student', ['program_id'], unique=False)
    op.create_index(op.f('ix_program_semester_student_semester_id'), 'program_semester_student', ['semester_id'], unique=False)
    op.create_index(op.f('ix_program_semester_student_student_id'), 'program_semester_student', ['student_id'], unique=False)
    op.add_column('payment', sa.Column('receipt_doc', sa.String(), nullable=True))
    op.add_column('payment', sa.Column('student_id', sa.UUID(), nullable=True))
    op.drop_index('ix_payment_amount', table_name='payment')
    op.drop_index('ix_payment_bank', table_name='payment')
    op.drop_index('ix_payment_branch', table_name='payment')
    op.drop_index('ix_payment_receipt_path', table_name='payment')
    op.drop_index('ix_payment_status', table_name='payment')
    op.drop_index('ix_payment_student_number', table_name='payment')
    op.drop_index('ix_payment_type', table_name='payment')
    op.create_index(op.f('ix_payment_receipt_doc'), 'payment', ['receipt_doc'], unique=False)
    op.create_index(op.f('ix_payment_student_id'), 'payment', ['student_id'], unique=False)
    op.drop_constraint('payment_student_number_fkey', 'payment', type_='foreignkey')
    op.create_foreign_key(None, 'payment', 'student', ['student_id'], ['student_id'])
    op.drop_column('payment', 'branch')
    op.drop_column('payment', 'receipt_path')
    op.drop_column('payment', 'type')
    op.drop_column('payment', 'student_number')
    op.drop_column('payment', 'status')
    op.drop_column('payment', 'amount')
    op.drop_column('payment', 'bank')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('bank', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('payment', sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('payment', sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('payment', sa.Column('student_number', sa.UUID(), autoincrement=False, nullable=True))
    op.add_column('payment', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('payment', sa.Column('receipt_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('payment', sa.Column('branch', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'payment', type_='foreignkey')
    op.create_foreign_key('payment_student_number_fkey', 'payment', 'student', ['student_number'], ['student_id'])
    op.drop_index(op.f('ix_payment_student_id'), table_name='payment')
    op.drop_index(op.f('ix_payment_receipt_doc'), table_name='payment')
    op.create_index('ix_payment_type', 'payment', ['type'], unique=False)
    op.create_index('ix_payment_student_number', 'payment', ['student_number'], unique=False)
    op.create_index('ix_payment_status', 'payment', ['status'], unique=False)
    op.create_index('ix_payment_receipt_path', 'payment', ['receipt_path'], unique=False)
    op.create_index('ix_payment_branch', 'payment', ['branch'], unique=False)
    op.create_index('ix_payment_bank', 'payment', ['bank'], unique=False)
    op.create_index('ix_payment_amount', 'payment', ['amount'], unique=False)
    op.drop_column('payment', 'student_id')
    op.drop_column('payment', 'receipt_doc')
    op.drop_index(op.f('ix_program_semester_student_student_id'), table_name='program_semester_student')
    op.drop_index(op.f('ix_program_semester_student_semester_id'), table_name='program_semester_student')
    op.drop_index(op.f('ix_program_semester_student_program_id'), table_name='program_semester_student')
    op.drop_table('program_semester_student')
    # ### end Alembic commands ###
