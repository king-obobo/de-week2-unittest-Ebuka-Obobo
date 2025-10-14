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
        print(self.glucose_level)
        

    def predict_action(self):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.
        """
        # TODO: decide what to do if glucose is too high, too low, or stable
        pass