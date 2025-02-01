from typing import (
    Any,
    List,
    Sequence,
    Type,
)

from sqlalchemy import (
    func,
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import Executable

from app.models.base import SQLModel


class SessionMixin:
    """Provides instance of database session."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session


class BaseService(SessionMixin):
    """Base class for application services."""


class BaseDataManager(SessionMixin):
    """Base data manager class responsible for operations over database."""

    async def add_one(self, model: Any):
        self.session.add(model)
        await self.session.commit()

    async def add_all(self, models: Sequence[Any]) -> None:
        self.session.add_all(models)
        await self.session.commit()

    async def get_one(self, select_stmt: Executable) -> Any:
        result = await self.session.execute(select_stmt)
        return result.scalar()

    async def get_all(self, select_stmt: Executable) -> List[Any]:
        result = await self.session.execute(select_stmt)
        return list(result.scalars().all())

    async def get_from_tvf(self, model: Type[SQLModel], *args: Any) -> List[Any]:
        """Query from table valued function.

        This is a wrapper function that can be used to retrieve data from
        table valued functions.

        Examples:
            from app.models.base import SQLModel

            class MyModel(SQLModel):
                __tablename__ = "function"
                __table_args__ = {"schema": "schema"}

                x: Mapped[int] = mapped_column("x", primary_key=True)
                y: Mapped[str] = mapped_column("y")
                z: Mapped[float] = mapped_column("z")

            # equivalent to "SELECT x, y, z FROM schema.function(1, 'AAA')"
            await BaseDataManager(session).get_from_tvf(MyModel, 1, "AAA")
        """

        return await self.get_all(self.select_from_tvf(model, *args))

    @staticmethod
    def select_from_tvf(model: Type[SQLModel], *args: Any) -> Executable:
        fn = getattr(getattr(func, model.schema()), model.table_name())
        stmt = select(fn(*args).table_valued(*model.fields()))
        return select(model).from_statement(stmt)
