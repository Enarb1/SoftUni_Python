from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver
    }

    VALID_FISH_TYPES = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish
    }

    def __init__(self):
        self.divers: list = []
        self.fish_list: list = []


    def dive_into_competition(self, diver_type: str, diver_name: str) -> str:

        try:
            diver = self.VALID_DIVER[diver_type](diver_name)
        except KeyError:
            return f"{diver_type} is not allowed in our competition."

        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."

        except StopIteration:
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float) -> str:

        try:
            fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."


    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool) -> str:
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver.name} hits a {fish.points}pt. {fish.name}."
            else:
                diver.miss(fish.time_to_catch)
                message = f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.update_health_status()

        return message

    def health_recovery(self) -> str:
        divers_with_health_issues = list(filter(lambda d: d.has_health_issue, self.divers))

        if divers_with_health_issues:
            for diver in divers_with_health_issues:
                diver.has_health_issue = False
                diver.renew_oxy()

        return f"Divers recovered: {len(divers_with_health_issues)}"

    def diver_catch_report(self,diver_name: str) -> str:
        diver = next(filter(lambda d: d.name == diver_name, self.divers))
        return f"**{diver.name} Catch Report**\n" + \
                "\n".join(f.fish_details() for f in diver.catch)


    def competition_statistics(self):
        divers_to_sort = filter(lambda d: not d.has_health_issue, self.divers)
        divers = sorted(divers_to_sort, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        return "**Nautical Catch Challenge Statistics**\n" + \
            "\n".join(str(d) for d in divers)





