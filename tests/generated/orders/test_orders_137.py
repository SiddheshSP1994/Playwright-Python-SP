import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8181", "title": "Orders scenario 8181", "data": {"sku": "SKU8181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8181@example.com", "threshold": 810}},
    {"id": "ORDERS-8182", "title": "Orders scenario 8182", "data": {"sku": "SKU8182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8182@example.com", "threshold": 820}},
    {"id": "ORDERS-8183", "title": "Orders scenario 8183", "data": {"sku": "SKU8183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8183@example.com", "threshold": 830}},
    {"id": "ORDERS-8184", "title": "Orders scenario 8184", "data": {"sku": "SKU8184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8184@example.com", "threshold": 840}},
    {"id": "ORDERS-8185", "title": "Orders scenario 8185", "data": {"sku": "SKU8185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8185@example.com", "threshold": 850}},
    {"id": "ORDERS-8186", "title": "Orders scenario 8186", "data": {"sku": "SKU8186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8186@example.com", "threshold": 860}},
    {"id": "ORDERS-8187", "title": "Orders scenario 8187", "data": {"sku": "SKU8187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8187@example.com", "threshold": 870}},
    {"id": "ORDERS-8188", "title": "Orders scenario 8188", "data": {"sku": "SKU8188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8188@example.com", "threshold": 880}},
    {"id": "ORDERS-8189", "title": "Orders scenario 8189", "data": {"sku": "SKU8189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8189@example.com", "threshold": 890}},
    {"id": "ORDERS-8190", "title": "Orders scenario 8190", "data": {"sku": "SKU8190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8190@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
