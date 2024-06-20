from sqlalchemy.orm import DeclarativeBase, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

class BaseModel(DeclarativeBase):
	uuid = uuid.uuid

class User(BaseModel):
	__tablename__ = 'users'

	user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	first_name = Column(String)
	last_name = Column(String)
	password = Column(String)
	email = Column(String)

class Place(BaseModel):
	place_id = Column(UUID(as_uuid=True), primary_key=True)
	user_id = Column(UUID(as_uuid=True)), ForeignKey(User.id)

class Review(BaseModel):
	__tablename__ = 'reviews'
	review_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	user_id = Column(UUID(as_uuid=True), ForeignKey(User.id))


	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" % (
			self.name, self.fullname, self.password)