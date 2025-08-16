import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8091", "title": "Analytics scenario 8091", "data": {"sku": "SKU8091", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8091@example.com", "threshold": 910}},
    {"id": "ANALYTICS-8092", "title": "Analytics scenario 8092", "data": {"sku": "SKU8092", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8092@example.com", "threshold": 920}},
    {"id": "ANALYTICS-8093", "title": "Analytics scenario 8093", "data": {"sku": "SKU8093", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8093@example.com", "threshold": 930}},
    {"id": "ANALYTICS-8094", "title": "Analytics scenario 8094", "data": {"sku": "SKU8094", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8094@example.com", "threshold": 940}},
    {"id": "ANALYTICS-8095", "title": "Analytics scenario 8095", "data": {"sku": "SKU8095", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8095@example.com", "threshold": 950}},
    {"id": "ANALYTICS-8096", "title": "Analytics scenario 8096", "data": {"sku": "SKU8096", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8096@example.com", "threshold": 960}},
    {"id": "ANALYTICS-8097", "title": "Analytics scenario 8097", "data": {"sku": "SKU8097", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8097@example.com", "threshold": 970}},
    {"id": "ANALYTICS-8098", "title": "Analytics scenario 8098", "data": {"sku": "SKU8098", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8098@example.com", "threshold": 980}},
    {"id": "ANALYTICS-8099", "title": "Analytics scenario 8099", "data": {"sku": "SKU8099", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8099@example.com", "threshold": 990}},
    {"id": "ANALYTICS-8100", "title": "Analytics scenario 8100", "data": {"sku": "SKU8100", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8100@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
