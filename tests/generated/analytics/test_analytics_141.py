import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8451", "title": "Analytics scenario 8451", "data": {"sku": "SKU8451", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8451@example.com", "threshold": 510}},
    {"id": "ANALYTICS-8452", "title": "Analytics scenario 8452", "data": {"sku": "SKU8452", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8452@example.com", "threshold": 520}},
    {"id": "ANALYTICS-8453", "title": "Analytics scenario 8453", "data": {"sku": "SKU8453", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8453@example.com", "threshold": 530}},
    {"id": "ANALYTICS-8454", "title": "Analytics scenario 8454", "data": {"sku": "SKU8454", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8454@example.com", "threshold": 540}},
    {"id": "ANALYTICS-8455", "title": "Analytics scenario 8455", "data": {"sku": "SKU8455", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8455@example.com", "threshold": 550}},
    {"id": "ANALYTICS-8456", "title": "Analytics scenario 8456", "data": {"sku": "SKU8456", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8456@example.com", "threshold": 560}},
    {"id": "ANALYTICS-8457", "title": "Analytics scenario 8457", "data": {"sku": "SKU8457", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8457@example.com", "threshold": 570}},
    {"id": "ANALYTICS-8458", "title": "Analytics scenario 8458", "data": {"sku": "SKU8458", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8458@example.com", "threshold": 580}},
    {"id": "ANALYTICS-8459", "title": "Analytics scenario 8459", "data": {"sku": "SKU8459", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8459@example.com", "threshold": 590}},
    {"id": "ANALYTICS-8460", "title": "Analytics scenario 8460", "data": {"sku": "SKU8460", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8460@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
