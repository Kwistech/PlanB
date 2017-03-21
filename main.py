# PlanB - Python 3.5 - Johnathon Kwisses (Kwistech)
from classes.getter import Getter
from classes.setter import Setter


def main():
    getter, setter = Getter(), Setter()
    data = getter.run()
    setter.run(data)

if __name__ == "__main__":
    main()
