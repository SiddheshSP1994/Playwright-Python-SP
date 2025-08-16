import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7701", "title": "Orders scenario 7701", "data": {"sku": "SKU7701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7701@example.com", "threshold": 10}},
    {"id": "ORDERS-7702", "title": "Orders scenario 7702", "data": {"sku": "SKU7702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7702@example.com", "threshold": 20}},
    {"id": "ORDERS-7703", "title": "Orders scenario 7703", "data": {"sku": "SKU7703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7703@example.com", "threshold": 30}},
    {"id": "ORDERS-7704", "title": "Orders scenario 7704", "data": {"sku": "SKU7704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7704@example.com", "threshold": 40}},
    {"id": "ORDERS-7705", "title": "Orders scenario 7705", "data": {"sku": "SKU7705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7705@example.com", "threshold": 50}},
    {"id": "ORDERS-7706", "title": "Orders scenario 7706", "data": {"sku": "SKU7706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7706@example.com", "threshold": 60}},
    {"id": "ORDERS-7707", "title": "Orders scenario 7707", "data": {"sku": "SKU7707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7707@example.com", "threshold": 70}},
    {"id": "ORDERS-7708", "title": "Orders scenario 7708", "data": {"sku": "SKU7708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7708@example.com", "threshold": 80}},
    {"id": "ORDERS-7709", "title": "Orders scenario 7709", "data": {"sku": "SKU7709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7709@example.com", "threshold": 90}},
    {"id": "ORDERS-7710", "title": "Orders scenario 7710", "data": {"sku": "SKU7710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7710@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
