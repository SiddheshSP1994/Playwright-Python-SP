import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8811", "title": "Analytics scenario 8811", "data": {"sku": "SKU8811", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8811@example.com", "threshold": 110}},
    {"id": "ANALYTICS-8812", "title": "Analytics scenario 8812", "data": {"sku": "SKU8812", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8812@example.com", "threshold": 120}},
    {"id": "ANALYTICS-8813", "title": "Analytics scenario 8813", "data": {"sku": "SKU8813", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8813@example.com", "threshold": 130}},
    {"id": "ANALYTICS-8814", "title": "Analytics scenario 8814", "data": {"sku": "SKU8814", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8814@example.com", "threshold": 140}},
    {"id": "ANALYTICS-8815", "title": "Analytics scenario 8815", "data": {"sku": "SKU8815", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8815@example.com", "threshold": 150}},
    {"id": "ANALYTICS-8816", "title": "Analytics scenario 8816", "data": {"sku": "SKU8816", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8816@example.com", "threshold": 160}},
    {"id": "ANALYTICS-8817", "title": "Analytics scenario 8817", "data": {"sku": "SKU8817", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8817@example.com", "threshold": 170}},
    {"id": "ANALYTICS-8818", "title": "Analytics scenario 8818", "data": {"sku": "SKU8818", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8818@example.com", "threshold": 180}},
    {"id": "ANALYTICS-8819", "title": "Analytics scenario 8819", "data": {"sku": "SKU8819", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8819@example.com", "threshold": 190}},
    {"id": "ANALYTICS-8820", "title": "Analytics scenario 8820", "data": {"sku": "SKU8820", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8820@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
