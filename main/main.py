from artificial_pancreas import ArtificialPancreasSystem


def main():
    system = ArtificialPancreasSystem(glucose_level=95)
    print("=================ArtificialPancreasSystem=========================")
    print(f"Your current Glucose level is: {system.glucose_level}mg/dL\n")
    
    print("===========Eating some food===============")
    system.meal(10)


if __name__ == "__main__":
    main()
