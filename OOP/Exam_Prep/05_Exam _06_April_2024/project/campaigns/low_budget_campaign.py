from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    CAMPAIGN_BUDGET: float = 2500.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, LowBudgetCampaign.CAMPAIGN_BUDGET, required_engagement)


    def check_eligibility(self, engagement_rate: float):
        return (self.required_engagement * 0.90) <= engagement_rate
