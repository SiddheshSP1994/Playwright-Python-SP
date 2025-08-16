import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8931", "title": "Analytics scenario 8931", "data": {"sku": "SKU8931", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8931@example.com", "threshold": 310}},
    {"id": "ANALYTICS-8932", "title": "Analytics scenario 8932", "data": {"sku": "SKU8932", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8932@example.com", "threshold": 320}},
    {"id": "ANALYTICS-8933", "title": "Analytics scenario 8933", "data": {"sku": "SKU8933", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8933@example.com", "threshold": 330}},
    {"id": "ANALYTICS-8934", "title": "Analytics scenario 8934", "data": {"sku": "SKU8934", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8934@example.com", "threshold": 340}},
    {"id": "ANALYTICS-8935", "title": "Analytics scenario 8935", "data": {"sku": "SKU8935", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8935@example.com", "threshold": 350}},
    {"id": "ANALYTICS-8936", "title": "Analytics scenario 8936", "data": {"sku": "SKU8936", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8936@example.com", "threshold": 360}},
    {"id": "ANALYTICS-8937", "title": "Analytics scenario 8937", "data": {"sku": "SKU8937", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8937@example.com", "threshold": 370}},
    {"id": "ANALYTICS-8938", "title": "Analytics scenario 8938", "data": {"sku": "SKU8938", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8938@example.com", "threshold": 380}},
    {"id": "ANALYTICS-8939", "title": "Analytics scenario 8939", "data": {"sku": "SKU8939", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8939@example.com", "threshold": 390}},
    {"id": "ANALYTICS-8940", "title": "Analytics scenario 8940", "data": {"sku": "SKU8940", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8940@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
