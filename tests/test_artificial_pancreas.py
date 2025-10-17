import pytest
from main.artificial_pancreas import ArtificialPancreasSystem

# Instantiating a reusable default sytem instance
@pytest.fixture
def system():
    return ArtificialPancreasSystem(glucose_level=100)


# ================= VALIDATING INPUT TYPES FOR THE system.meal METHOD====================
@pytest.mark.parametrize("bad_inputs", ["ten", None, [], {}])
def test_meal_type_valueerror(system, bad_inputs):
    with pytest.raises(ValueError):
        system.meal(bad_inputs)


@pytest.mark.parametrize("negative_inputs", [-1, -2, -400])
def test_negative_carb_valueerror(system, negative_inputs):
    with pytest.raises(ValueError):
        system.meal(negative_inputs)


# ================= VALIDATING INPUT TYPES FOR THE system.exercise METHOD====================
@pytest.mark.parametrize("bad_inputs", ["five", None, [], {}])
def test_negative_exercise_type_valueerror(system, bad_inputs):
    with pytest.raises(ValueError):
        system.exercise(bad_inputs)
        
        
@pytest.mark.parametrize("negative_inputs", [-5, -54, -600])
def test_negative_exercise_valueerror(system, negative_inputs):
    with pytest.raises(ValueError):
        system.exercise(negative_inputs)


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
    # TODO: Excercise for some mins and check if 
    pass