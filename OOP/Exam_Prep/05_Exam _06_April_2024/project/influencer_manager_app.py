from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign

class InfluencerManagerApp:

    VALID_INFLUENCER_TYPE = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer,
    }

    VALID_CAMPAIGN_TYPES = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers: list = []
        self.campaigns: list = []


    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):

        if not self.__valid_influencer_type(influencer_type):
            return f"{influencer_type} is not an allowed influencer type."

        if self.__get_influencer(username) is not None:
            return f"{username} is already registered."

        new_influencer = self.VALID_INFLUENCER_TYPE[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)

        return f"{username} is successfully registered as a {influencer_type}."


    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):

        if not self.__valid_campaign(campaign_type):
            return f"{campaign_type} is not a valid campaign type."

        if self.__get_campaign(campaign_id) is not None:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)

        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."


    def participate_in_campaign(self, influencer_username: str, campaign_id: int):

        if self.__get_influencer(influencer_username) is None:
            return f"Influencer '{influencer_username}' not found."

        influencer = self.__get_influencer(influencer_username)

        if self.__get_campaign(campaign_id) is None:
            return f"Campaign with ID {campaign_id} not found."

        campaign = self.__get_campaign(campaign_id)

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the "
                    f"eligibility criteria for the campaign with ID {campaign_id}.")

        payment = influencer.calculate_payment(campaign)

        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)

            return (f"Influencer '{influencer_username}' "
                    f"has successfully participated in the campaign with ID {campaign_id}.")


    def calculate_total_reached_followers(self):

        total_reached_followers = {}

        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                reached_followers = influencer.reached_followers(type(campaign).__name__)
                total_reached_followers[campaign] = total_reached_followers.get(campaign, 0) + reached_followers

        return total_reached_followers


    def influencer_campaign_report(self, username: str):
        influencer = self.__get_influencer(username)
        return influencer.display_campaigns_participated()


    def campaign_statistics(self):
        total_reached_followers = self.calculate_total_reached_followers()
        sorted_campaign = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        campaign_stats = [
            f"  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, "
            f"Total budget: ${c.budget:.2f}, Total reached followers: {total_reached_followers.get(c,0)}"
            for c in sorted_campaign
        ]

        return f"$$ Campaign Statistics $$\n" + "\n".join(campaign_stats)



    def __get_influencer(self, username: str):
        influencer = [i for i in self.influencers if i.username == username]

        return influencer[0] if influencer else None

    def __get_campaign(self, campaign_id: int):
        campaign = [c for c in self.campaigns if c.campaign_id == campaign_id]

        return campaign[0] if campaign else None

    def __valid_campaign(self, campaign_type):
        return campaign_type in self.VALID_CAMPAIGN_TYPES.keys()

    def __valid_influencer_type(self, influencer_type):
        return influencer_type in self.VALID_INFLUENCER_TYPE.keys()
