# PlanB - Python 3.5 - Johnathon Kwisses (Kwistech)
from classes.getter import Getter
from classes.setter import Setter


def main():
    """Main function that runs Getter and Setter."""
    # Create Getter and Setter objects
    getter, setter = Getter(), Setter()

    # Retrieve data from files within data directory
    data = getter.run()

    # Uses data to backup user files
    setter.run(data)

if __name__ == "__main__":
    main()
