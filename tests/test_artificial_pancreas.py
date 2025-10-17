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


# ====================VALIDATING RETURN TYPES FOR THE system.meal METHOD====================
def test_meal_return_vals(system):
    prev_glucose_level = system.glucose_level
    carbs, curr_glucose_level = system.meal(100)
    assert curr_glucose_level ==  prev_glucose_level + (carbs * ArtificialPancreasSystem.GLUCOSE_PER_CARB)
    assert carbs == 100


# ====================VALIDATING STATE CHANGE FOR THE glucose_level parameter using system.meal METHOD====================
def test_meal_change_glucose_level(system):
    prev_glucose_level = system.glucose_level
    _, curr_glucose_level = system.meal(100)
    assert curr_glucose_level >  prev_glucose_level


# ====================VALIDATING RETURN TYPES FOR THE system.exercise METHOD====================
def test_exercise_return_vals(system):
    prev_glucose_level = system.glucose_level
    
    #1. Regular Excercise Duration
    duration, curr_glucose_level = system.exercise(100)
    assert curr_glucose_level == prev_glucose_level - (duration * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN)
    
    #Extremely High duration of exercise
    duration, curr_glucose_level = system.exercise(10000)
    assert curr_glucose_level == 50


# ====================VALIDATING STATE CHANGE FOR THE glucose_level parameter using system.exercise METHOD====================
def test_meal_change_glucose_level(system):
    prev_glucose_level = system.glucose_level
    _, curr_glucose_level = system.exercise(100)
    assert curr_glucose_level <  prev_glucose_level


# ====================VALIDATING RETURN VALUE FOR THE correction_units  METHOD====================
def test_correcion_units(system):
    system.glucose_level = 200
    calculated_correction_unit = abs(system.glucose_level - system.target_glucose)
    system_correction_unit = system.correction_units()
    assert calculated_correction_unit == system_correction_unit


# ====================VALIDATING STATE CHANGE FOR THE _set_min_glucose METHOD====================
def test_set_min_glucose(system):
    system.glucose_level = 10
    system._set_min_glucose()
    assert system.glucose_level == 50


# ====================VALIDATING STATE CHANGE FOR THE self.total_insulin_delivered attribute and the deliver_insulin METHOD====================
def test_insulin_delivered_attribute(system):
    #Testing with High Insulin levels
    system.glucose_level = 200
    pre_total_insulin_delivered = system.total_insulin_delivered
    prev_glucose_level = system.glucose_level
    
    # Delivering Insulim
    system.deliver_insulin()
    
    # Testing for my Values
    assert prev_glucose_level > system.glucose_level
    assert system.total_insulin_delivered > pre_total_insulin_delivered
    
    # Testing with Lower than target insulin levels
    system.glucose_level = 60
    pre_total_insulin_delivered = system.total_insulin_delivered
    prev_glucose_level = system.glucose_level
    
    # delivering Insulin
    system.deliver_insulin()
    
    # Testing my values
    assert system.glucose_level == 50


# ====================VALIDATING RETURN VALUES FOR THE predict_action METHOD====================
@pytest.mark.parametrize("glucose_level, expected_action", [
    (100, "maintain"),
    (109, "maintain"),
    (120, "deliver_insulin"),
    (200, "deliver_insulin"),
    (80, "warn_low_glucose"),
    (60, "warn_low_glucose")
])
def test_predict_action(system, glucose_level, expected_action):
    system.glucose_level = glucose_level
    action, _ = system.predict_action()
    assert action == expected_action
    
def test_predict_action_delivery(system):
    system.glucose_level = 300
    prev_glucose_level = system.glucose_level
    _, adjusted_glucose_value = system.predict_action()
    assert prev_glucose_level > adjusted_glucose_value
    
# ====================TESTING FOR MULTIPLE SEQUENTIAL EVENTS====================
def test_meal_exercise_insulin(system):
    before_meal_glucose_level = system.glucose_level
    system.meal(200)
    after_meal_glucose_level = system.glucose_level
    
    before_exercise_glucose_level = system.glucose_level
    system.exercise(20)
    after_exercise_glucose_level = system.glucose_level
    
    before_insulin_glucose_level = system.glucose_level
    system.deliver_insulin()
    after_insulin_glucose_level = system.glucose_level
    
    assert before_meal_glucose_level < after_meal_glucose_level
    assert after_meal_glucose_level == before_exercise_glucose_level
    assert before_exercise_glucose_level > after_exercise_glucose_level
    assert after_exercise_glucose_level == before_insulin_glucose_level
    assert before_insulin_glucose_level > after_insulin_glucose_level