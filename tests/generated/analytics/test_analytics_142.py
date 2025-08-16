import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8511", "title": "Analytics scenario 8511", "data": {"sku": "SKU8511", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8511@example.com", "threshold": 110}},
    {"id": "ANALYTICS-8512", "title": "Analytics scenario 8512", "data": {"sku": "SKU8512", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8512@example.com", "threshold": 120}},
    {"id": "ANALYTICS-8513", "title": "Analytics scenario 8513", "data": {"sku": "SKU8513", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8513@example.com", "threshold": 130}},
    {"id": "ANALYTICS-8514", "title": "Analytics scenario 8514", "data": {"sku": "SKU8514", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8514@example.com", "threshold": 140}},
    {"id": "ANALYTICS-8515", "title": "Analytics scenario 8515", "data": {"sku": "SKU8515", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8515@example.com", "threshold": 150}},
    {"id": "ANALYTICS-8516", "title": "Analytics scenario 8516", "data": {"sku": "SKU8516", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8516@example.com", "threshold": 160}},
    {"id": "ANALYTICS-8517", "title": "Analytics scenario 8517", "data": {"sku": "SKU8517", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8517@example.com", "threshold": 170}},
    {"id": "ANALYTICS-8518", "title": "Analytics scenario 8518", "data": {"sku": "SKU8518", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8518@example.com", "threshold": 180}},
    {"id": "ANALYTICS-8519", "title": "Analytics scenario 8519", "data": {"sku": "SKU8519", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8519@example.com", "threshold": 190}},
    {"id": "ANALYTICS-8520", "title": "Analytics scenario 8520", "data": {"sku": "SKU8520", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8520@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
