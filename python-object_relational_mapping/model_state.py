#!/usr/bin/python3
""" Module define a state class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ The class """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)