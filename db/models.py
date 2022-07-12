from datetime import datetime as dt
from sqlalchemy.schema import Column
from sqlalchemy import DateTime, Integer, String, ForeignKey, Text, Boolean
from db.database import Base


class Account(Base):
    __tablename__ = "accounts"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    created_at = Column("created_at", DateTime, default=dt.now(), nullable=False)
    updated_at = Column(
        "updated_at",
        DateTime,
        default=dt.now(),
        onupdate=dt.now(),
        nullable=False,
    )


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    name = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    hashed_password = Column(String(100))
    role_id = Column(Integer, ForeignKey("roles.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))
    created_at = Column("created_at", DateTime, default=dt.now(), nullable=False)
    updated_at = Column(
        "updated_at",
        DateTime,
        default=dt.now(),
        onupdate=dt.now(),
        nullable=False,
    )


class Role(Base):
    __tablename__ = "roles"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    created_at = Column("created_at", DateTime, default=dt.now(), nullable=False)
    updated_at = Column(
        "updated_at",
        DateTime,
        default=dt.now(),
        onupdate=dt.now(),
        nullable=False,
    )


class Team(Base):
    __tablename__ = "teams"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    name = Column(String(30), nullable=False)
    description = Column(Text())
    created_at = Column("created_at", DateTime, default=dt.now(), nullable=False)
    updated_at = Column(
        "updated_at",
        DateTime,
        default=dt.now(),
        onupdate=dt.now(),
        nullable=False,
    )


class Quest(Base):
    __tablename__ = "quests"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(Text(), nullable=True)
    reward = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Boolean, nullable=False)
    created_at = Column("created_at", DateTime, default=dt.now(), nullable=False)
    updated_at = Column(
        "updated_at",
        DateTime,
        default=dt.now(),
        onupdate=dt.now(),
        nullable=False,
    )


class ApproveRequest(Base):
    __tablename__ = "approve_requests"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    description = Column(Text(), nullable=True)
    quest_id = Column(Integer, ForeignKey("quests.id"))
    applicant_id = Column(Integer, ForeignKey("users.id"))
    authorizer_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column("created_at", DateTime, default=dt.now(), nullable=False)
    updated_at = Column(
        "updated_at",
        DateTime,
        default=dt.now(),
        onupdate=dt.now(),
        nullable=False,
    )


class Penalty(Base):
    __tablename__ = "penalties"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text(), nullable=True)
    penalty = Column(Integer, nullable=False)


class IssuedPenalty(Base):
    __tablename__ = "issued_penalties"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    authorizer_id = Column(Integer, ForeignKey("users.id"))
    team_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column("created_at", DateTime, default=dt.now(), nullable=False)
    updated_at = Column(
        "updated_at",
        DateTime,
        default=dt.now(),
        onupdate=dt.now(),
        nullable=False,
    )
