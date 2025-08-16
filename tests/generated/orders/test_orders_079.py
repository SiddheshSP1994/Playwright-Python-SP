import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4701", "title": "Orders scenario 4701", "data": {"sku": "SKU4701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4701@example.com", "threshold": 10}},
    {"id": "ORDERS-4702", "title": "Orders scenario 4702", "data": {"sku": "SKU4702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4702@example.com", "threshold": 20}},
    {"id": "ORDERS-4703", "title": "Orders scenario 4703", "data": {"sku": "SKU4703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4703@example.com", "threshold": 30}},
    {"id": "ORDERS-4704", "title": "Orders scenario 4704", "data": {"sku": "SKU4704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4704@example.com", "threshold": 40}},
    {"id": "ORDERS-4705", "title": "Orders scenario 4705", "data": {"sku": "SKU4705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4705@example.com", "threshold": 50}},
    {"id": "ORDERS-4706", "title": "Orders scenario 4706", "data": {"sku": "SKU4706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4706@example.com", "threshold": 60}},
    {"id": "ORDERS-4707", "title": "Orders scenario 4707", "data": {"sku": "SKU4707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4707@example.com", "threshold": 70}},
    {"id": "ORDERS-4708", "title": "Orders scenario 4708", "data": {"sku": "SKU4708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4708@example.com", "threshold": 80}},
    {"id": "ORDERS-4709", "title": "Orders scenario 4709", "data": {"sku": "SKU4709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4709@example.com", "threshold": 90}},
    {"id": "ORDERS-4710", "title": "Orders scenario 4710", "data": {"sku": "SKU4710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4710@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
