import os

from typing import List, Dict, Any

from pyosrd.agents import Agent


def test_agent(use_case_straight_line):
    use_case_straight_line.add_delay(
        'train0',
        60.,
        60.,
    )

    class TestAgent(Agent):
        def stops(self, osrd) -> List[Dict[str, Any]]:
            return [{
                'train': 0,
                'position': 1000.,
                'duration': 100.,
            }]

    regulated = use_case_straight_line.regulate(agent=TestAgent('test'))
    assert os.path.exists(os.path.join('tmp', 'delayed', 'test'))
    arrival_time = \
        use_case_straight_line.points_encountered_by_train(0)[-1]['t_base']

    regulated_arrival_time = \
        regulated.points_encountered_by_train(0)[-1]['t_base']
    assert regulated_arrival_time - arrival_time > 160.
    use_case_straight_line.reset_delays()
