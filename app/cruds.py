from fabric.common.crud import CRUDBase
from app import models, schemas


class UserCrud(CRUDBase[models.User, schemas.UserBase]):
    def __init__(self):
        super().__init__(models.User)


class IndicatorCrud(CRUDBase[models.Indicator, schemas.IndicatorBase]):
    def __init__(self):
        super().__init__(models.Indicator)


class PollCrud(CRUDBase[models.Poll, schemas.PollBase]):
    def __init__(self):
        super().__init__(models.Poll)


class VoteCrud(CRUDBase[models.Vote, schemas.VoteBase]):
    def __init__(self):
        super().__init__(models.Vote)


class ScheduleCrud(CRUDBase[models.Schedule, schemas.ScheduleBase]):
    def __init__(self):
        super().__init__(models.Schedule)
