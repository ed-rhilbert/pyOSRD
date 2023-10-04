import json
import os
import shutil

import pytest


def test_add_delay_existing_file(use_case_straight_line):
    with open(os.path.join('tmp', 'delays.json'), "w") as outfile:
        json.dump([], outfile)
    use_case_straight_line.add_delay(
        'train0',
        60.,
        60.,
    )
    expected = [
        {
            "train_id": 'train0',
            "time_threshold": 60.,
            "delay": 60.,
        }
    ]
    with open(os.path.join('tmp', 'delays.json'), "r") as file:
        delays = json.load(file)

    assert delays == expected
    os.remove(os.path.join('tmp', 'delays.json'))


def test_add_delay_no_preexisting_file(use_case_straight_line):
    use_case_straight_line.add_delay(
        'train0',
        60.,
        60.,
    )
    expected = [
        {
            "train_id": 'train0',
            "time_threshold": 60.,
            "delay": 60.,
        }
    ]
    with open(os.path.join('tmp', 'delays.json'), "r") as file:
        delays = json.load(file)

    assert delays == expected
    os.remove(os.path.join('tmp', 'delays.json'))


def test_add_delay_in_results(use_case_straight_line):
    use_case_straight_line.add_delay(
        'train0',
        60.,
        60.,
    )
    arrival_time = \
        use_case_straight_line.points_encountered_by_train(0)[-1]['t_base']
    use_case_straight_line.add_delays_in_results()
    new_arrival_time = \
        use_case_straight_line.points_encountered_by_train(0)[-1]['t_base']
    assert pytest.approx(new_arrival_time - arrival_time) == 60.
    os.remove(os.path.join('tmp', 'delays.json'))


def test_delayed_simulation(use_case_straight_line):
    use_case_straight_line.add_delay(
        'train0',
        60.,
        60.,
    )
    arrival_time = \
        use_case_straight_line.points_encountered_by_train(0)[-1]['t_base']
    delayed_case = use_case_straight_line.delayed()
    assert os.path.exists(os.path.join('tmp', 'delayed', 'results.json'))
    delayed_arrival_time = \
        delayed_case.points_encountered_by_train(0)[-1]['t_base']
    assert pytest.approx(delayed_arrival_time - arrival_time) == 60.
    os.remove(os.path.join('tmp', 'delays.json'))
    shutil.rmtree(os.path.join('tmp', 'delayed'), ignore_errors=True)


def test_reset_delays(use_case_straight_line):
    use_case_straight_line.add_delay(
        'train0',
        60.,
        60.,
    )
    use_case_straight_line.delayed()
    use_case_straight_line.reset_delays()
    assert not os.path.exists(os.path.join('tmp', 'delayed'))
    assert not os.path.exists(os.path.join('tmp', 'delays_json'))
