from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    CAMPAIGN_BUDGET: float = 5000.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, HighBudgetCampaign.CAMPAIGN_BUDGET, required_engagement)


    def check_eligibility(self, engagement_rate: float):
        return (self.required_engagement * 1.20) <= engagement_rate