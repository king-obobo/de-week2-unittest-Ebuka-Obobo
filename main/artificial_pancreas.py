# My main class for this project

class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""
        
    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise


    def __init__(self, glucose_level: int|float, insulin_sensitivity: int|float=1.0, target_glucose: int|float=100, tolerance: int|float=10, total_insulin_delivered = 0):
        # TODO: initialize class attributes here
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        self.total_insulin_delivered = total_insulin_delivered
        

    def meal(self, carbs: float| int):
        """Simulate a meal event (input feature: carbs)."""
        # TODO: increase glucose based on carbs eaten
        if not isinstance(carbs, (float, int)):
            raise ValueError(f"Invalid carbs input: expected a number, got {type(carbs).__name__}")
            
        if carbs < 0:
            raise ValueError(f"{carbs} cannot be less than Zero")
        
        self.glucose_level += carbs * ArtificialPancreasSystem.GLUCOSE_PER_CARB
        return carbs, self.glucose_level

    def exercise(self, duration: float| int):
        """Simulate physical activity (input feature: duration)."""
        # TODO: decrease glucose based on duration of exercise
        if not isinstance(duration, (float, int)):
            raise ValueError(f"Invalid duration input: expected a number, got {type(duration).__name__}")
            
        if duration < 0:
            raise ValueError(f"{duration} cannot be less than Zero")
        
        self.glucose_level -= duration * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN
        self._set_min_glucose()
        return duration, self.glucose_level
        
    
    def correction_units(self):
        return (self.glucose_level - self.target_glucose) / self.insulin_sensitivity
    
    
    def _set_min_glucose(self):
        if self.glucose_level <= 50:
            self.glucose_level = 50
        
    
    def deliver_insulin(self):
        # To deliver Insulin, I would need to first calculate the amount of insulin to deliver
        # Then deliver the insulin, adjust the total insulin delivered and adjust the glucose level accordingly
        if self.glucose_level > (self.target_glucose + self.tolerance):
            correction_units = self.correction_units()
            self.glucose_level -= correction_units
            self.total_insulin_delivered += correction_units
            self._set_min_glucose()
        else:
            pass
        
        

    def predict_action(self):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.
        """
        # TODO: decide what to do if glucose is too high, too low, or stable
        # If gluuose level is too high, the system should deliver Insulin
        if self.glucose_level > (self.target_glucose + self.tolerance):
            print(f"The glucose level is high")
            self.deliver_insulin()
            return (f"deliver_insulin", self.glucose_level)
            
            
        elif self.glucose_level in range(self.target_glucose, self.target_glucose+self.tolerance+1):
            print("Glucose level is within Range")
            return (f"maintain", self.glucose_level)
            
        else:
            print(f"WARNING !!!, Your Glucose level is low !!")
            return (f"warn_low_glucose", self.glucose_level)