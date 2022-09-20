import json
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, UniqueConstraint, JSON, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def transform_to_dict(model):
    res = {c.name: getattr(model, c.name) for c in model.__table__.columns}
    return json.loads(json.dumps(res, default=str))


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "email", name="uc_email"
        ),
    )

    def as_dict(self):
        return transform_to_dict(model=self)


class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    payment_method = Column(Boolean, default=False, server_default="False", nullable=False)
    phone_number = Column(String(200), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "user_id", name="uc_user_id"
        ),
    )

    def as_dict(self):
        return transform_to_dict(model=self)


class ClientRate(Base):
    __tablename__ = "client_rate"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    average = Column(String(20), nullable=False)
    comment = Column(String(500), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "client_id", name="uc_client_id"
        ),
    )

    def as_dict(self):
        return transform_to_dict(model=self)


class Reservation(Base):
    __tablename__ = "reservation"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    salon_id = Column(Integer, ForeignKey("salon.id"), nullable=False)
    prestation_id = Column(Integer, ForeignKey("prestation.id"), nullable=False)


class Salon(Base):
    __tablename__ = "salon"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    name = Column(String(200), nullable=False)
    description = Column(String(500), nullable=False)
    address_id = Column(Integer, ForeignKey("address.id"), nullable=False)
    opening_hours = Column(JSON, nullable=False)
    type_id = Column(Integer, ForeignKey("type.id"), nullable=False)
    phone_number = Column(String(200), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "name", name="uc_name_salon"
        ),
    )


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    salon_id = Column(Integer, ForeignKey("salon.id"), nullable=False)
    is_manager = Column(Boolean, default=False, server_default="False", nullable=False)


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    longitude = Column(String(200), nullable=False)
    latitude = Column(String(200), nullable=False)
    address = Column(JSON, nullable=False)
    zoom = Column(Integer)
    quartier = Column(String(200), nullable=False)


class Type(Base):
    __tablename__ = "type"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    name = Column(String(200), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "name", name="uc_name_type"
        ),
    )


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    name = Column(String(200), nullable=False)
    type_id = Column(Integer, ForeignKey("type.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "name", name="uc_name_category"
        ),
    )


class Prestation(Base):
    __tablename__ = "prestation"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    name = Column(String(200), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    description = Column(String(200), nullable=False)
    duration = Column(JSON)

    __table_args__ = (
        UniqueConstraint(
            "name", name="uc_name_prestation"
        ),
    )


class Image(Base):
    __tablename__ = "image"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    salon_id = Column(Integer, ForeignKey("salon.id"), nullable=False)
    file_url = Column(String(200), nullable=False)
    is_main = Column(Boolean, default=False, server_default="False", nullable=False)


class SalonRate(Base):
    __tablename__ = "salon_rate"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    salon_id = Column(Integer, ForeignKey("salon.id"), nullable=False)
    average = Column(String(20), nullable=False)
    comment = Column(String(500), nullable=False)

