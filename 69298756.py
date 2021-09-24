import json
import requests


def plan1A1C():
    body = {
        "payload": {
            "data": {
                "organization_code": "TEST",
                "quote_id": 71728,
                "quote_token": "odQ53i3SxCANUR68Lry3",
                "session_token": "odQ53i3SxCANUR68Lry3",
                "partner_code": "TEST",
                "category_code": "TEST",
                "insured": [
                    {
                        "person_id": 45820,
                        "name": None,
                        "occupation": None,
                        "annual_income": None,
                        "phone_number": "8789538796",
                        "email": None,
                        "age": 40,
                        "dob": "07-09-1981",
                        "gender": None,
                        "nominee_name": " ",
                        "nominee_dob": None,
                        "nominee_age": None,
                        "nominee_gender": None,
                        "appointee_name": " ",
                        "appointee_dob": None,
                        "relationship_with_appointee": None,
                        "appointee_gender": None,
                        "relationship_with_nominee": None,
                        "relation_with_primary_member": "self",
                        "height": None,
                        "weight": None,
                        "salutation": None,
                        "marital_status": None
                    },
                    {
                        "person_id": 45821,
                        "name": None,
                        "occupation": None,
                        "annual_income": None,
                        "phone_number": "8789538796",
                        "email": None,
                        "age": 10,
                        "dob": "07-09-2011",
                        "gender": None,
                        "nominee_name": " ",
                        "nominee_dob": None,
                        "nominee_age": None,
                        "nominee_gender": None,
                        "appointee_name": " ",
                        "appointee_dob": None,
                        "relationship_with_appointee": None,
                        "appointee_gender": None,
                        "relationship_with_nominee": None,
                        "relation_with_primary_member": "kid-1",
                        "height": None,
                        "weight": None,
                        "salutation": None,
                        "marital_status": None
                    }

                ],
                "primary_member_age": 40,
                "sum_insured": 100000,
                "pin_code": "751008",
                "payment_frequency": "SINGLE",
                "payment_option": None,
                "limited_pay": None,
                "policy_paying_term": None,
                "tobacco_habit": None,
                "risk_profile": None,
                "maturity_benefit_type": None,
                "investment_goal": None,
                "investment_amount": None,
                "cover_list": None,
                "insurance_cover_list": None,
                "posp": {
                    "name": "abcd",
                    "user_id": "98765432",
                    "pan": None,
                    "aadhar": None,
                    "level": {
                        "id": 41,
                        "partner_id": 52,
                        "role": "TEST",
                        "code": "TEST",
                        "superior_role_id": None,
                        "path": "//41",
                        "created_at": "2021-06-11T17:48:01.000+05:30",
                        "updated_at": "2021-06-12T16:42:40.000+05:30"
                    },
                    "staf_type": "POSP"
                },
                "product_code": "TEST",
                "insurance_code": "TEST",
                "tenure": 1
            },
            "config": {
                "coi_url": "https://developer.cholainsurance.com/endpoint/Health-flexiretail/v1.0.0/PolicySchedule",
                "password": "in5uR@nceAnan0",
                "plan_url": "https://developer.cholainsurance.com/endpoint/Health-flexiretail/v1.0.0/PremiumComputation",
                "username": "ptrn_anandinsurance",
                "token_url": "https://developer.cholainsurance.com/endpoint/token",
                "grant_type": "password",
                "policy_url": "https://developer.cholainsurance.com/endpoint/Health-flexiretail/v1.0.0/PolicyGeneration",
                "proposal_url": "https://developer.cholainsurance.com/endpoint/Health-flexiretail/v1.0.0/ProposalSave",
                "PaymentOption": "A",
                "header_password": "Auv9XfPYReebvef6fm2uSX8F3f0a",
                "header_username": "IQ0wIXe6Xz94HIHxcIhyof6Kqdoa",
                "IntermediaryCode": "2002954741760001",
                "UniqueTransactionID": "8765456711111111112232"
            }
        },
        "insurance_company_code": "HDFC_MEDICAL",
        "ic": "HDFC_MEDICAL",
        "insurance_code": "CHOLA_FLEXI_HEALTH",
        "product_code": "CHOLA_FLEXI_HEALTH",
        "category_code": "HEALTH_RETAIL",
        "callbackUrl": "https://api.iifl.test.com/api_gateway_callbacks/plans"
        }
    return body

print(json.dumps(plan1A1C(), indent=4))
url = "https://akse.cloud"
response = requests.post(url, json=plan1A1C())
print(response)