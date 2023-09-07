from policyengine_canada.model_api import *


class infirm_dependant_amount_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan Infirm Dependant Amount Eligibility"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-lp-22e.pdf#page=6",
        "https://pubsaskdev.blob.core.windows.net/pubsask-prod/806/I2-01.pdf#page=13,14,15",
    )
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.infirm_dependant_amount

        dependant = person("is_dependant", period)
        age = person("age", period)
        age_eligibility = age <= p.age_threshold
    
        dependants_income = person("individual_net_income", period)
        income_eligibility = dependants_income <= p.higher_income_threshold

        return age_eligibility & income_eligibility