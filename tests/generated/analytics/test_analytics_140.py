import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8391", "title": "Analytics scenario 8391", "data": {"sku": "SKU8391", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8391@example.com", "threshold": 910}},
    {"id": "ANALYTICS-8392", "title": "Analytics scenario 8392", "data": {"sku": "SKU8392", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8392@example.com", "threshold": 920}},
    {"id": "ANALYTICS-8393", "title": "Analytics scenario 8393", "data": {"sku": "SKU8393", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8393@example.com", "threshold": 930}},
    {"id": "ANALYTICS-8394", "title": "Analytics scenario 8394", "data": {"sku": "SKU8394", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8394@example.com", "threshold": 940}},
    {"id": "ANALYTICS-8395", "title": "Analytics scenario 8395", "data": {"sku": "SKU8395", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8395@example.com", "threshold": 950}},
    {"id": "ANALYTICS-8396", "title": "Analytics scenario 8396", "data": {"sku": "SKU8396", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8396@example.com", "threshold": 960}},
    {"id": "ANALYTICS-8397", "title": "Analytics scenario 8397", "data": {"sku": "SKU8397", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8397@example.com", "threshold": 970}},
    {"id": "ANALYTICS-8398", "title": "Analytics scenario 8398", "data": {"sku": "SKU8398", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8398@example.com", "threshold": 980}},
    {"id": "ANALYTICS-8399", "title": "Analytics scenario 8399", "data": {"sku": "SKU8399", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8399@example.com", "threshold": 990}},
    {"id": "ANALYTICS-8400", "title": "Analytics scenario 8400", "data": {"sku": "SKU8400", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8400@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
