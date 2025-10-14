# My main class for this project

class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""
        
    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise


    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        # TODO: initialize class attributes here
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        

    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""
        # TODO: increase glucose based on carbs eaten
        self.glucose_level += carbs * ArtificialPancreasSystem.GLUCOSE_PER_CARB
        print(f"After eating {carbs}G worth of carbs, your new glucose level is: {self.glucose_level}mg/dL\n")

    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration)."""
        # TODO: decrease glucose based on duration of exercise
        self.glucose_level -= duration * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN
        self.set_correct_glucose()
        print(f"{duration * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN}")
        print(f"Aftre excercising for {duration} mins, your new glucose level is {self.glucose_level} mg/dL \n")
        
    
    def  correction_units(self):
        return (self.glucose_level - self.target_glucose) / self.insulin_sensitivity
    
    
    def set_correct_glucose(self):
        if self.glucose_level <= 50:
            self.glucose_level = 50
        
    
    def deliver_insulin(self):
        # To deliver Insulin, I would need to first calculate the amount of insulin to deliver
        # Then deliver the insulin and adjust the glucose level accordingly
        correction_units = self.correction_units()
        self.glucose_level -= correction_units
        self.set_correct_glucose()
        
        print(f"Delivered {correction_units} Units of Insulin. Your gluose level is now {self.glucose_level} mg/dL")
        

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