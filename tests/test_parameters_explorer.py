import numpy as np
from collections import namedtuple
from parameters_explorer import ParametersExplorer


def test_pe_example1():
    explorer = ParametersExplorer()
    explorer.add_parameter("rsi_period", 14, np.arange(start=10, stop=20, step=1), int)
    explorer.add_parameter(
        "rsi_min", 30.0, np.linspace(start=0, stop=100, num=11), float
    )
    explorer.add_parameter(
        "rsi_max", 70.0, np.linspace(start=0, stop=100, num=11), float
    )
    # explorer.add_parameter("dir", "BUY", ["BUY", "SELL"], str)
    assert explorer.count_runs == 1210
    explorer.add_constraint(lambda p: p.rsi_min < p.rsi_max)
    assert explorer.count_runs == 550


def test_pe_example2_noexploration():
    explorer = ParametersExplorer()
    explorer.add_parameter("rsi_period", 14)
    explorer.add_parameter("rsi_min", 30.0)
    explorer.add_parameter("rsi_max", 70.0)
    assert explorer.count_runs == 1
    parameters = [p for p in explorer.parameters()]
    assert parameters[0].rsi_period == 14
    assert parameters[0].rsi_min == 30.0
    assert parameters[0].rsi_max == 70.0


def test_pe_example3_noparameters():
    explorer = ParametersExplorer()
    assert explorer.count_runs == 1
    parameters = [p for p in explorer.parameters()]
    assert parameters[0]._asdict() == {}


def test_pe_example4_noexploration_assert_type():
    explorer = ParametersExplorer()
    explorer.add_parameter("fast_period", 8)
    explorer.add_parameter("slow_period", 12)
    explorer.add_parameter("signal_period", 10)
    explorer.add_parameter("rogers_satchell_vol_period", 30)
    explorer.add_constraint(lambda p: p.fast_period < p.slow_period)
    parameters = [p for p in explorer.parameters()]
    assert isinstance(parameters[0].fast_period, int)
    assert isinstance(parameters[0].slow_period, int)
    assert isinstance(parameters[0].signal_period, int)
    assert isinstance(parameters[0].rogers_satchell_vol_period, int)
