from policyengine_canada.model_api import *


class climate_action_incentive_post_rural(Variable):
    value_type = float
    entity = Household
    label = "Canada Climate Action Incentive after rural supplement"
    unit = CAD
    documentation = "Universal amount without adjustment based on AFNI"
    definition_period = YEAR

    def formula(household, period, parameters):
        amount = household("climate_action_incentive_pre_rural", period)
        rural = household("is_rural", period)
        rural_amount = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action_incentive.rural
        return where(rural, amount + (amount * rural_amount), amount)
