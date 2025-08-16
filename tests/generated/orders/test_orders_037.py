import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2181", "title": "Orders scenario 2181", "data": {"sku": "SKU2181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2181@example.com", "threshold": 810}},
    {"id": "ORDERS-2182", "title": "Orders scenario 2182", "data": {"sku": "SKU2182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2182@example.com", "threshold": 820}},
    {"id": "ORDERS-2183", "title": "Orders scenario 2183", "data": {"sku": "SKU2183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2183@example.com", "threshold": 830}},
    {"id": "ORDERS-2184", "title": "Orders scenario 2184", "data": {"sku": "SKU2184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2184@example.com", "threshold": 840}},
    {"id": "ORDERS-2185", "title": "Orders scenario 2185", "data": {"sku": "SKU2185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2185@example.com", "threshold": 850}},
    {"id": "ORDERS-2186", "title": "Orders scenario 2186", "data": {"sku": "SKU2186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2186@example.com", "threshold": 860}},
    {"id": "ORDERS-2187", "title": "Orders scenario 2187", "data": {"sku": "SKU2187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2187@example.com", "threshold": 870}},
    {"id": "ORDERS-2188", "title": "Orders scenario 2188", "data": {"sku": "SKU2188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2188@example.com", "threshold": 880}},
    {"id": "ORDERS-2189", "title": "Orders scenario 2189", "data": {"sku": "SKU2189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2189@example.com", "threshold": 890}},
    {"id": "ORDERS-2190", "title": "Orders scenario 2190", "data": {"sku": "SKU2190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2190@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
