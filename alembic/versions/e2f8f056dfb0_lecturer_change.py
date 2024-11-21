"""lecturer change

Revision ID: e2f8f056dfb0
Revises: 0d2b9fe59d5a
Create Date: 2024-09-23 17:27:30.826878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2f8f056dfb0'
down_revision: Union[str, None] = '0d2b9fe59d5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_student_enrolled_courses_course_id', table_name='student_enrolled_courses')
    op.drop_index('ix_student_enrolled_courses_semester_id', table_name='student_enrolled_courses')
    op.drop_index('ix_student_enrolled_courses_student_id', table_name='student_enrolled_courses')
    op.drop_table('student_enrolled_courses')
    op.add_column('lecturer', sa.Column('lecturer_image', sa.String(), nullable=True))
    op.create_index(op.f('ix_lecturer_lecturer_image'), 'lecturer', ['lecturer_image'], unique=False)
    op.drop_index('ix_student_newStudent_id', table_name='student')
    op.drop_index('ix_student_semester_id', table_name='student')
    op.drop_constraint('student_semester_id_fkey', 'student', type_='foreignkey')
    op.drop_constraint('student_newStudent_id_fkey', 'student', type_='foreignkey')
    op.drop_column('student', 'newStudent_id')
    op.drop_column('student', 'semester_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('semester_id', sa.UUID(), autoincrement=False, nullable=True))
    op.add_column('student', sa.Column('newStudent_id', sa.UUID(), autoincrement=False, nullable=True))
    op.create_foreign_key('student_newStudent_id_fkey', 'student', 'new_student', ['newStudent_id'], ['newStudent_id'])
    op.create_foreign_key('student_semester_id_fkey', 'student', 'semester', ['semester_id'], ['semester_id'])
    op.create_index('ix_student_semester_id', 'student', ['semester_id'], unique=False)
    op.create_index('ix_student_newStudent_id', 'student', ['newStudent_id'], unique=False)
    op.drop_index(op.f('ix_lecturer_lecturer_image'), table_name='lecturer')
    op.drop_column('lecturer', 'lecturer_image')
    op.create_table('student_enrolled_courses',
    sa.Column('course_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('student_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('semester_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('course_id', 'student_id', 'semester_id', name='student_enrolled_courses_pkey')
    )
    op.create_index('ix_student_enrolled_courses_student_id', 'student_enrolled_courses', ['student_id'], unique=False)
    op.create_index('ix_student_enrolled_courses_semester_id', 'student_enrolled_courses', ['semester_id'], unique=False)
    op.create_index('ix_student_enrolled_courses_course_id', 'student_enrolled_courses', ['course_id'], unique=False)
    # ### end Alembic commands ###
