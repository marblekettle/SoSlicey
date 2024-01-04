from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import String

class Base(DeclarativeBase):
	pass

class Order(Base):
	__tablename__ = "order"
	id: Mapped[int] = mapped_column(primary_key=True)

class Item(Base):
	__tablename__ = "item"
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(50))

class OrderItem(Base):
	__tablename__ = "order_item"
	id: Mapped[int] = mapped_column(primary_key=True)
	order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
	item_id: Mapped[int] = mapped_column(ForeignKey("item.id"))
	number: Mapped[int]
