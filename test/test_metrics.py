import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from quantstats import reports
from mock_data import DailyReturns


def test_report():
    returns = DailyReturns().generate().returns
    reports.metrics(returns, mode="full", benchmark="SPY")




