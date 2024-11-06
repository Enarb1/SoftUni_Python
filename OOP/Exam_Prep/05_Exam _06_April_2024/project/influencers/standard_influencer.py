from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT = 0.45
    MULTIPLIER = {
        "HighBudgetCampaign": 1.2,
        "LowBudgetCampaign": 0.9
    }
    def calculate_payment(self, campaign):
        return campaign.budget * StandardInfluencer.INITIAL_PAYMENT

    def reached_followers(self, campaign_type: str):
        return int((self.followers * self.engagement_rate) * self.MULTIPLIER[campaign_type])