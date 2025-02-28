from typing import List

from project.peaks.base_peak import BasePeak

class ArcticPeak(BasePeak):

    def get_recommended_gear(self) -> List[str]:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self) -> str: #TODO try with mapper
        if self.elevation > 3000:
            return "Extreme"
        elif 2000 <=  self.elevation <= 3000:
            return "Advanced"