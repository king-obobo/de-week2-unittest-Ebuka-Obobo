from artificial_pancreas import ArtificialPancreasSystem


def main():
    system = ArtificialPancreasSystem(glucose_level=80)
    print("=================ArtificialPancreasSystem=========================")
    print(f"Your current Glucose level is: {system.glucose_level}mg/dL\n")
    
    print("===========Eating some food===============")
    system.meal(80)
    
    print("\n============Excercising================")
    system.exercise(300)
    
    print("============Predicting Action================")
    action, level = system.predict_action()
    print(action, level)    

if __name__ == "__main__":
    main()
