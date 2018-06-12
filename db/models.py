"""
Base and App specific models are
defined here
"""

from sqlalchemy import Column, Integer, TIMESTAMP, func, DateTime, create_engine
from sqlalchemy import String, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker

from db.config import Config

session = scoped_session(sessionmaker())


class BaseModel(object):
    """
    Base model, from which all the other
    models will be inherited
    """

    @declared_attr
    def __tablename__(cls):
        """
        Set db name for all the tables
        :return: string, db_name
        """
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    modified_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())


Base = declarative_base(cls=BaseModel)


class Bundle(Base):
    """
    Model for storing/accessing the Bundles
    """
    device_uuid = Column(String(100), nullable=False, index=True)
    sensor_type = Column(String(100), nullable=False, index=True)
    sensor_value = Column(Float, nullable=False, index=True)
    sensor_reading_time = Column(BigInteger, nullable=False, index=True)

    def __init__(self, device_uuid, sensor_type, sensor_value, sensor_reading_time):
        """
        Create instance with the defined params
        :param name: string
        :param prep_time: integer
        :param difficulty: float
        :param vegetarian: bool
        """
        self.device_uuid = device_uuid
        self.sensor_type = sensor_type
        self.sensor_value = sensor_value
        self.sensor_reading_time = sensor_reading_time

    def to_dict(self):
        """
        Return dictionary of instance
        :return: dict, instance properties
        """
        return {
            "device_uuid": self.device_uuid,
            "sensor_type": self.sensor_type,
            "sensor_value": self.sensor_value,
            "sensor_reading_time": self.sensor_reading_time,
        }


config = Config()
engine = create_engine(config.connection_string, echo=False)
session.configure(bind=engine)
