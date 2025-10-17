import pytest
from main.artificial_pancreas import ArtificialPancreasSystem


@pytest.fixture
def system():
    return ArtificialPancreasSystem(glucose_level=100)


def test_glucose_increases_after_meal(system):
    #TODO: eat a meal and check if glucose levels increases
    curr_glucose = system.glucose_level
    system.meal(80)
    assert  system.glucose_level > curr_glucose


def test_glucose_never_below_min(system):
    # TODO: Exrcise for a very long duration and assert thet glucose level does not go below 50
    system.exercise(1000)
    assert system.glucose_level >= 50
    


def test_glucose_decreases_after_excercise(system):
    # TODO
    pass