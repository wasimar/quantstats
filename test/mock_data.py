from dataclasses import dataclass
from datetime import timedelta, datetime
from random import randint, uniform
import pandas as pd


# pick random date between 2010 and 2020
def random_date():
    start = datetime(2010, 1, 1, 00, 00, 00)
    end = datetime(2020, 1, 1, 00, 00, 00)
    return start + (end - start) * randint(0, 1000) / 1000


@dataclass
class DailyReturns:
    """Generate random daily returns for random number of days."""
    start_date: datetime = random_date().date()
    end_date: datetime = start_date + timedelta(days=randint(3, 300))
    returns: pd.DataFrame = None

    def generate(self) -> pd.DataFrame:
        series = pd.date_range(start=self.start_date,
                               end=self.end_date, freq='B')
        self.returns = pd.DataFrame(
            [uniform(-0.1, 0.1) for i in range(len(series))], index=series, columns=['returns'])
        # set 0 at multiple random index
        self.returns.iloc[randint(0, len(self.returns)-1)] = 0.0
        # DataFrame to Series
        self.returns = self.returns['returns']
        return self
