import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-6231", "title": "Analytics scenario 6231", "data": {"sku": "SKU6231", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6231@example.com", "threshold": 310}},
    {"id": "ANALYTICS-6232", "title": "Analytics scenario 6232", "data": {"sku": "SKU6232", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6232@example.com", "threshold": 320}},
    {"id": "ANALYTICS-6233", "title": "Analytics scenario 6233", "data": {"sku": "SKU6233", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6233@example.com", "threshold": 330}},
    {"id": "ANALYTICS-6234", "title": "Analytics scenario 6234", "data": {"sku": "SKU6234", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6234@example.com", "threshold": 340}},
    {"id": "ANALYTICS-6235", "title": "Analytics scenario 6235", "data": {"sku": "SKU6235", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6235@example.com", "threshold": 350}},
    {"id": "ANALYTICS-6236", "title": "Analytics scenario 6236", "data": {"sku": "SKU6236", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6236@example.com", "threshold": 360}},
    {"id": "ANALYTICS-6237", "title": "Analytics scenario 6237", "data": {"sku": "SKU6237", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6237@example.com", "threshold": 370}},
    {"id": "ANALYTICS-6238", "title": "Analytics scenario 6238", "data": {"sku": "SKU6238", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6238@example.com", "threshold": 380}},
    {"id": "ANALYTICS-6239", "title": "Analytics scenario 6239", "data": {"sku": "SKU6239", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6239@example.com", "threshold": 390}},
    {"id": "ANALYTICS-6240", "title": "Analytics scenario 6240", "data": {"sku": "SKU6240", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6240@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
