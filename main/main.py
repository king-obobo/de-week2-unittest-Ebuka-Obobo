from artificial_pancreas import ArtificialPancreasSystem


def main():
    system = ArtificialPancreasSystem(glucose_level=80)
    print("=================ArtificialPancreasSystem=========================")
    print(f"Your current Glucose level is: {system.glucose_level}mg/dL\n")
    
    print("===========Eating some food===============")
    carbs_eaten, curr_glucose_level = system.meal(80.0)
    print(f"After eating {carbs_eaten}G of food, the current glucose level is {curr_glucose_level}mg/dL")
    
    print("\n============Excercising================")
    excercise_duration, curr_glucose_level = system.exercise(300)
    print(f"After excercising for {excercise_duration} mins, your new glucose level is {curr_glucose_level} mg/dL \n")
    
    print("\n============Predicting Action================")
    action, level = system.predict_action()
    print(action, level)    
    
    print("\n============Delivering Insulin when Glucose is Low================")
    system.glucose_level = 60
    print(system.glucose_level)
    system.deliver_insulin()
    print(system.glucose_level)  
    
    print("\n============Delivering Insulin when Glucose is High================")
    system.glucose_level = 200
    print(system.glucose_level)
    system.deliver_insulin()
    print(system.glucose_level)  

if __name__ == "__main__":
    main()
