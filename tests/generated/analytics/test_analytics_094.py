import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-5631", "title": "Analytics scenario 5631", "data": {"sku": "SKU5631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5631@example.com", "threshold": 310}},
    {"id": "ANALYTICS-5632", "title": "Analytics scenario 5632", "data": {"sku": "SKU5632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5632@example.com", "threshold": 320}},
    {"id": "ANALYTICS-5633", "title": "Analytics scenario 5633", "data": {"sku": "SKU5633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5633@example.com", "threshold": 330}},
    {"id": "ANALYTICS-5634", "title": "Analytics scenario 5634", "data": {"sku": "SKU5634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5634@example.com", "threshold": 340}},
    {"id": "ANALYTICS-5635", "title": "Analytics scenario 5635", "data": {"sku": "SKU5635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5635@example.com", "threshold": 350}},
    {"id": "ANALYTICS-5636", "title": "Analytics scenario 5636", "data": {"sku": "SKU5636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5636@example.com", "threshold": 360}},
    {"id": "ANALYTICS-5637", "title": "Analytics scenario 5637", "data": {"sku": "SKU5637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5637@example.com", "threshold": 370}},
    {"id": "ANALYTICS-5638", "title": "Analytics scenario 5638", "data": {"sku": "SKU5638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5638@example.com", "threshold": 380}},
    {"id": "ANALYTICS-5639", "title": "Analytics scenario 5639", "data": {"sku": "SKU5639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5639@example.com", "threshold": 390}},
    {"id": "ANALYTICS-5640", "title": "Analytics scenario 5640", "data": {"sku": "SKU5640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5640@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
