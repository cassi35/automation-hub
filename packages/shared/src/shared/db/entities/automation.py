from datetime import datetime

from shared.db.settings.base import Base
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column,relationship,Mapped

# class AutomationModel(Base):
#     __tablename__ = "automation"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(30), nullable=False)
#     description = Column(Text, nullable=True)

#     trigger = Column(
#         Enum(
#             "github_actions",
#             "system",
#             name="automation_trigger",
#         ),
#         nullable=False,
#     )

#     status = Column(
#         Enum(
#             "active",
#             "deactive",
#             name="automation_status",
#         ),
#         nullable=False,
#     )

#     executions = relationship(
#         "ExecutionModel",
#         back_populates="automation",
#         cascade="all, delete-orphan",
#     )


class AutomationModel(Base):
    __tablename__ = "automation"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    trigger: Mapped[str] = mapped_column(
        Enum(
            "github_actions",
            "system",
            name="automation_trigger",
        ),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        Enum(
            "active",
            "deactive",
            name="automation_status",
        ),
        nullable=False,
    )

    executions: Mapped[list["ExecutionModel"]] = relationship(
        back_populates="automation",
        cascade="all, delete-orphan",
    )

    # class ExecutionModel(Base):
    #     __tablename__ = "executions"

    #     id = Column(Integer, primary_key=True)

    #     automation_id = Column(
    #         Integer,
    #         ForeignKey("automation.id"),
    #         nullable=False,
    #     )

    #     status = Column(
    #         Enum(
    #             "process",
    #             "failed",
    #             "success",
    #             name="execution_status",
    #         ),
    #         nullable=False,
    #     )

    #     start_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    #     end_at = Column(DateTime, nullable=True)

    #     automation = relationship(
    #         "AutomationModel",
    #         back_populates="executions",
    #     )

    #     steps = relationship(
    #         "StepModel",
    #         back_populates="execution",
    #         cascade="all, delete-orphan",
    #     )

class ExecutionModel(Base):
    __tablename__ = "executions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    automation_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("automation.id"),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        Enum(
            "process",
            "failed",
            "success",
            name="execution_status",
        ),
        nullable=False,
    )

    start_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    end_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    automation: Mapped["AutomationModel"] = relationship(
        back_populates="executions",
    )

    steps: Mapped[list["StepModel"]] = relationship(
        back_populates="execution",
        cascade="all, delete-orphan",
    )
# class StepModel(Base):
#     __tablename__ = "steps"

#     id = Column(Integer, primary_key=True)

#     name = Column(String(30), nullable=False)

#     status = Column(
#         Enum(
#             "running",
#             "stopped",
#             "failed",
#             name="step_status",
#         ),
#         nullable=False,
#     )

#     execution_id = Column(
#         Integer,
#         ForeignKey("executions.id"),
#         nullable=False,
#     )

#     execution = relationship(
#         "ExecutionModel",
#         back_populates="steps",
#     )

#     metrics = relationship(
#         "MetricModel",
#         back_populates="step",
#         cascade="all, delete-orphan",
#     )


# class MetricModel(Base):
#     __tablename__ = "metrics"

#     id = Column(Integer, primary_key=True)

#     execution_at = Column(
#         DateTime,
#         default=datetime.utcnow,
#         nullable=False,
#     )

#     name = Column(
#         Enum(
#             "duration",
#             name="metric_name",
#         ),
#         nullable=False,
#     )

#     value = Column(Integer, nullable=False)

#     step_id = Column(
#         Integer,
#         ForeignKey("steps.id"),
#         nullable=False,
#     )

#     step = relationship(
#         "StepModel",
#         back_populates="metrics",
#     )


class StepModel(Base):
    __tablename__ = "steps"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        Enum(
            "running",
            "stopped",
            "failed",
            name="step_status",
        ),
        nullable=False,
    )

    execution_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("executions.id"),
        nullable=False,
    )

    execution: Mapped["ExecutionModel"] = relationship(
        "ExecutionModel",
        back_populates="steps",
    )

    metrics: Mapped[list["MetricModel"]] = relationship(
        "MetricModel",
        back_populates="step",
        cascade="all, delete-orphan",
    )


class MetricModel(Base):
    __tablename__ = "metrics"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    execution_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        Enum(
            "duration",
            name="metric_name",
        ),
        nullable=False,
    )

    value: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    step_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("steps.id"),
        nullable=False,
    )

    step: Mapped["StepModel"] = relationship(
        "StepModel",
        back_populates="metrics",
    )