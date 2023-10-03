import shutil

import pytest

from pyosrd import OSRD


@pytest.fixture(scope='session')
def osrd_cvg_dvg_missing_sim():
    yield OSRD(
        results_json="missing.json",
        simulation_json="missing.json",
    )
    shutil.rmtree('tmp', ignore_errors=True)


@pytest.fixture(scope='session')
def osrd_cvg_dvg_before_run():
    yield OSRD(results_json="missing.json")
    shutil.rmtree('tmp', ignore_errors=True)


@pytest.fixture(scope='session')
def use_case_cvg_dvg():
    yield OSRD(dir='tmp', use_case='cvg_dvg')
    shutil.rmtree('tmp', ignore_errors=True)


@pytest.fixture(scope='session')
def use_case_station_capacity2():
    yield OSRD(dir='tmp', use_case='station_capacity2')
    shutil.rmtree('tmp', ignore_errors=True)


@pytest.fixture(scope='session')
def use_case_point_switch():
    yield OSRD(dir='tmp', use_case='point_switch')
    shutil.rmtree('tmp', ignore_errors=True)


@pytest.fixture(scope='session')
def use_case_straight_line():
    yield OSRD(dir='tmp', use_case='straight_line')
    shutil.rmtree('tmp', ignore_errors=True)
