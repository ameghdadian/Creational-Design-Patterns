from abc import ABC, abstractmethod
from enum import Enum


class WorkoutPlan:
    pass


class BuildMuscleWorkout(WorkoutPlan):
    def __str__(self):
        return "Planning workout to build muscle"


class WeighLossWorkout(WorkoutPlan):
    def __str__(self):
        return "Planning workout to lose weight"


class StrengthTrainingWorkout(WorkoutPlan):
    def __str__(self):
        return "Planning workout to buildup strength"


class MealPlan:
    pass


class WeighLossMealPlan(MealPlan):
    def __str__(self):
        return "Planning meal to lose weight"


class BuildMuscleMealPlan(MealPlan):
    def __str__(self):
        return "Planning meal to build muscle"


class StrengthTrainingMealPlan(MealPlan):
    def __str__(self):
        return "Planning meal to buildup strength"


class Goal(Enum):
    WEIGHT_LOSS = 0
    BUILD_MUSCLE = 1
    STRENGTH_TRAINING = 2


class Goal(ABC):
    @abstractmethod
    def create_workout(self):
        pass

    @abstractmethod
    def create_meal_plan(self):
        pass


class BuildMuscleGoal(Goal):
    def create_workout(self):
        return BuildMuscleWorkout()

    def create_meal_plan(self):
        return BuildMuscleMealPlan()


class WeighLossGoal(Goal):
    def create_workout(self):
        return WeighLossWorkout()

    def create_meal_plan(self):
        return WeighLossMealPlan()


class StrengthTrainingGoal(Goal):
    def create_workout(self):
        return StrengthTrainingWorkout()

    def create_meal_plan(self):
        return StrengthTrainingMealPlan()


class HomePage:
    def set_goal(self, goal: Goal):
        meal_plan = goal.create_meal_plan()
        workout_plan = goal.create_workout()

        print(workout_plan)
        print(meal_plan)


def main():
    homepage = HomePage()
    homepage.set_goal(StrengthTrainingGoal())


if __name__ == '__main__':
    main()
