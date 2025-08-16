import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4791", "title": "Analytics scenario 4791", "data": {"sku": "SKU4791", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4791@example.com", "threshold": 910}},
    {"id": "ANALYTICS-4792", "title": "Analytics scenario 4792", "data": {"sku": "SKU4792", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4792@example.com", "threshold": 920}},
    {"id": "ANALYTICS-4793", "title": "Analytics scenario 4793", "data": {"sku": "SKU4793", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4793@example.com", "threshold": 930}},
    {"id": "ANALYTICS-4794", "title": "Analytics scenario 4794", "data": {"sku": "SKU4794", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4794@example.com", "threshold": 940}},
    {"id": "ANALYTICS-4795", "title": "Analytics scenario 4795", "data": {"sku": "SKU4795", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4795@example.com", "threshold": 950}},
    {"id": "ANALYTICS-4796", "title": "Analytics scenario 4796", "data": {"sku": "SKU4796", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4796@example.com", "threshold": 960}},
    {"id": "ANALYTICS-4797", "title": "Analytics scenario 4797", "data": {"sku": "SKU4797", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4797@example.com", "threshold": 970}},
    {"id": "ANALYTICS-4798", "title": "Analytics scenario 4798", "data": {"sku": "SKU4798", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4798@example.com", "threshold": 980}},
    {"id": "ANALYTICS-4799", "title": "Analytics scenario 4799", "data": {"sku": "SKU4799", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4799@example.com", "threshold": 990}},
    {"id": "ANALYTICS-4800", "title": "Analytics scenario 4800", "data": {"sku": "SKU4800", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4800@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
