import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-5811", "title": "Analytics scenario 5811", "data": {"sku": "SKU5811", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5811@example.com", "threshold": 110}},
    {"id": "ANALYTICS-5812", "title": "Analytics scenario 5812", "data": {"sku": "SKU5812", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5812@example.com", "threshold": 120}},
    {"id": "ANALYTICS-5813", "title": "Analytics scenario 5813", "data": {"sku": "SKU5813", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5813@example.com", "threshold": 130}},
    {"id": "ANALYTICS-5814", "title": "Analytics scenario 5814", "data": {"sku": "SKU5814", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5814@example.com", "threshold": 140}},
    {"id": "ANALYTICS-5815", "title": "Analytics scenario 5815", "data": {"sku": "SKU5815", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5815@example.com", "threshold": 150}},
    {"id": "ANALYTICS-5816", "title": "Analytics scenario 5816", "data": {"sku": "SKU5816", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5816@example.com", "threshold": 160}},
    {"id": "ANALYTICS-5817", "title": "Analytics scenario 5817", "data": {"sku": "SKU5817", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5817@example.com", "threshold": 170}},
    {"id": "ANALYTICS-5818", "title": "Analytics scenario 5818", "data": {"sku": "SKU5818", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5818@example.com", "threshold": 180}},
    {"id": "ANALYTICS-5819", "title": "Analytics scenario 5819", "data": {"sku": "SKU5819", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5819@example.com", "threshold": 190}},
    {"id": "ANALYTICS-5820", "title": "Analytics scenario 5820", "data": {"sku": "SKU5820", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5820@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
