from utils.base_enums import BaseEnum


class HallStatusEnum(BaseEnum):
    PENDING = 'pending'
    PROGRESS = 'progress'
    COMPLETED = 'completed'
    CANCELED = 'canceled'
