import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0231", "title": "Analytics scenario 231", "data": {"sku": "SKU231", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user231@example.com", "threshold": 310}},
    {"id": "ANALYTICS-0232", "title": "Analytics scenario 232", "data": {"sku": "SKU232", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user232@example.com", "threshold": 320}},
    {"id": "ANALYTICS-0233", "title": "Analytics scenario 233", "data": {"sku": "SKU233", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user233@example.com", "threshold": 330}},
    {"id": "ANALYTICS-0234", "title": "Analytics scenario 234", "data": {"sku": "SKU234", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user234@example.com", "threshold": 340}},
    {"id": "ANALYTICS-0235", "title": "Analytics scenario 235", "data": {"sku": "SKU235", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user235@example.com", "threshold": 350}},
    {"id": "ANALYTICS-0236", "title": "Analytics scenario 236", "data": {"sku": "SKU236", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user236@example.com", "threshold": 360}},
    {"id": "ANALYTICS-0237", "title": "Analytics scenario 237", "data": {"sku": "SKU237", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user237@example.com", "threshold": 370}},
    {"id": "ANALYTICS-0238", "title": "Analytics scenario 238", "data": {"sku": "SKU238", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user238@example.com", "threshold": 380}},
    {"id": "ANALYTICS-0239", "title": "Analytics scenario 239", "data": {"sku": "SKU239", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user239@example.com", "threshold": 390}},
    {"id": "ANALYTICS-0240", "title": "Analytics scenario 240", "data": {"sku": "SKU240", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user240@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
