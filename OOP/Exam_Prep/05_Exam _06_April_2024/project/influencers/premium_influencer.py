from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign



class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT = 0.85
    MULTIPLIER = {
        "HighBudgetCampaign": 1.5,
        "LowBudgetCampaign": 0.8
    }

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * PremiumInfluencer.INITIAL_PAYMENT

    def reached_followers(self, campaign_type: str):
        return int((self.followers * self.engagement_rate) * self.MULTIPLIER[campaign_type])