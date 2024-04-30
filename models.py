from typing import Optional

from pandas import DataFrame
from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class University(Base):
    __tablename__ = 'universities'

    id: Mapped[int] = mapped_column(primary_key=True)
    university_name: Mapped[str] = mapped_column(String(50))

    @staticmethod
    def from_series(s):
        _university = University()
        if s:
            _university.university_name = s
        else:
            _university.university_name = ' '
        return _university


class Speciality(Base):
    __tablename__ = 'specialities'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    code: Mapped[str]

    @staticmethod
    def from_series(s):
        _speciality = Speciality()
        _speciality.name = s['speciality_name']
        _speciality.code = s['speciality_code']
        return _speciality

class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    zno_ukrainian: Mapped[Optional[float]]
    zno_math: Mapped[Optional[float]]
    zno_biology: Mapped[Optional[float]]
    zno_history: Mapped[Optional[float]]
    zno_foreign: Mapped[Optional[float]]
    zno_geography: Mapped[Optional[float]]
    zno_chemistry: Mapped[Optional[float]]
    gpa: Mapped[Optional[float]]

    def __str__(self):
        return f'name:  {self.name}, id: {self.id}'

    @staticmethod
    def from_series(s):
        _student = Student()
        _student.name = s['name']
        _student.zno_ukrainian = s['zno_ukrainian']
        _student.zno_math = s['zno_math']
        _student.zno_biology = s['zno_biology']
        _student.zno_history = s['zno_history']
        _student.zno_foreign = s['zno_foreign']
        _student.zno_chemistry = s['zno_chemistry']
        _student.zno_geography = s['zno_geography']
        _student.gpa = s['gpa']
        return _student


class Application(Base):
    __tablename__ = 'applications'

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    university_id: Mapped[int] = mapped_column(ForeignKey('universities.id'))
    speciality_id: Mapped[int] = mapped_column(ForeignKey('specialities.id'))

    student = relationship('Student')
    university = relationship('University')
    speciality = relationship('Speciality')

    status: Mapped[str]
    year: Mapped[int]
    total_score: Mapped[float]
    rank: Mapped[int]
    priority: Mapped[int]
    village_ratio: Mapped[bool]
    industry_ratio: Mapped[bool]

    def __str__(self):
        return f'id: {self.id}, student: {self.student.name}, university: {self.university.university_name}'

if __name__ == '__main__':
    engine = create_engine('sqlite:///students_copy.db')

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = select(Application)

        response = session.scalars(query)

        for app in response:
            if app.student.zno_ukrainian > 190:
                print(app)


