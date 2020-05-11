#! /usr/bin/env python3
#
# 2020-05-08 
# Colton Grainger 
# CC-0 Public Domain

"""
2020-05-08 acceptance test
"""

from context import imagearchive
from imagearchive.schema import Base, Archive, Platform, Document, Image
from imagearchive.core import setup_directories, setup_database_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date

engine = setup_database_engine()
ingest_dir, data_dir, output_dir = setup_directories()

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
