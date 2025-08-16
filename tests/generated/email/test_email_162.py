import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9701", "title": "Email scenario 9701", "data": {"sku": "SKU9701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9701@example.com", "threshold": 10}},
    {"id": "EMAIL-9702", "title": "Email scenario 9702", "data": {"sku": "SKU9702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9702@example.com", "threshold": 20}},
    {"id": "EMAIL-9703", "title": "Email scenario 9703", "data": {"sku": "SKU9703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9703@example.com", "threshold": 30}},
    {"id": "EMAIL-9704", "title": "Email scenario 9704", "data": {"sku": "SKU9704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9704@example.com", "threshold": 40}},
    {"id": "EMAIL-9705", "title": "Email scenario 9705", "data": {"sku": "SKU9705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9705@example.com", "threshold": 50}},
    {"id": "EMAIL-9706", "title": "Email scenario 9706", "data": {"sku": "SKU9706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9706@example.com", "threshold": 60}},
    {"id": "EMAIL-9707", "title": "Email scenario 9707", "data": {"sku": "SKU9707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9707@example.com", "threshold": 70}},
    {"id": "EMAIL-9708", "title": "Email scenario 9708", "data": {"sku": "SKU9708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9708@example.com", "threshold": 80}},
    {"id": "EMAIL-9709", "title": "Email scenario 9709", "data": {"sku": "SKU9709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9709@example.com", "threshold": 90}},
    {"id": "EMAIL-9710", "title": "Email scenario 9710", "data": {"sku": "SKU9710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9710@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
