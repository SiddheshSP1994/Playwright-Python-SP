import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8631", "title": "Analytics scenario 8631", "data": {"sku": "SKU8631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8631@example.com", "threshold": 310}},
    {"id": "ANALYTICS-8632", "title": "Analytics scenario 8632", "data": {"sku": "SKU8632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8632@example.com", "threshold": 320}},
    {"id": "ANALYTICS-8633", "title": "Analytics scenario 8633", "data": {"sku": "SKU8633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8633@example.com", "threshold": 330}},
    {"id": "ANALYTICS-8634", "title": "Analytics scenario 8634", "data": {"sku": "SKU8634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8634@example.com", "threshold": 340}},
    {"id": "ANALYTICS-8635", "title": "Analytics scenario 8635", "data": {"sku": "SKU8635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8635@example.com", "threshold": 350}},
    {"id": "ANALYTICS-8636", "title": "Analytics scenario 8636", "data": {"sku": "SKU8636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8636@example.com", "threshold": 360}},
    {"id": "ANALYTICS-8637", "title": "Analytics scenario 8637", "data": {"sku": "SKU8637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8637@example.com", "threshold": 370}},
    {"id": "ANALYTICS-8638", "title": "Analytics scenario 8638", "data": {"sku": "SKU8638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8638@example.com", "threshold": 380}},
    {"id": "ANALYTICS-8639", "title": "Analytics scenario 8639", "data": {"sku": "SKU8639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8639@example.com", "threshold": 390}},
    {"id": "ANALYTICS-8640", "title": "Analytics scenario 8640", "data": {"sku": "SKU8640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8640@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
