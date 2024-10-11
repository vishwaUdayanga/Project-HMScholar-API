"""On delete cascade on certain models

Revision ID: abb23bb71618
Revises: 45c03edcdfd6
Create Date: 2024-10-05 12:12:17.444347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abb23bb71618'
down_revision: Union[str, None] = '45c03edcdfd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('answer_question_id_fkey', 'answer', type_='foreignkey')
    op.create_foreign_key(None, 'answer', 'question', ['question_id'], ['question_id'], ondelete='CASCADE')
    op.drop_constraint('course_announcement_course_id_fkey', 'course_announcement', type_='foreignkey')
    op.create_foreign_key(None, 'course_announcement', 'course', ['course_id'], ['course_id'], ondelete='CASCADE')
    op.drop_constraint('course_material_section_id_fkey', 'course_material', type_='foreignkey')
    op.create_foreign_key(None, 'course_material', 'section', ['section_id'], ['section_id'], ondelete='CASCADE')
    op.drop_constraint('question_quiz_id_fkey', 'question', type_='foreignkey')
    op.create_foreign_key(None, 'question', 'quiz', ['quiz_id'], ['quiz_id'], ondelete='CASCADE')
    op.drop_constraint('quiz_section_id_fkey', 'quiz', type_='foreignkey')
    op.create_foreign_key(None, 'quiz', 'section', ['section_id'], ['section_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'quiz', type_='foreignkey')
    op.create_foreign_key('quiz_section_id_fkey', 'quiz', 'section', ['section_id'], ['section_id'])
    op.drop_constraint(None, 'question', type_='foreignkey')
    op.create_foreign_key('question_quiz_id_fkey', 'question', 'quiz', ['quiz_id'], ['quiz_id'])
    op.drop_constraint(None, 'course_material', type_='foreignkey')
    op.create_foreign_key('course_material_section_id_fkey', 'course_material', 'section', ['section_id'], ['section_id'])
    op.drop_constraint(None, 'course_announcement', type_='foreignkey')
    op.create_foreign_key('course_announcement_course_id_fkey', 'course_announcement', 'course', ['course_id'], ['course_id'])
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.create_foreign_key('answer_question_id_fkey', 'answer', 'question', ['question_id'], ['question_id'])
    # ### end Alembic commands ###