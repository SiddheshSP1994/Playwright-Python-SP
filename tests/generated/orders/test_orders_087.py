import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5181", "title": "Orders scenario 5181", "data": {"sku": "SKU5181", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5181@example.com", "threshold": 810}},
    {"id": "ORDERS-5182", "title": "Orders scenario 5182", "data": {"sku": "SKU5182", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5182@example.com", "threshold": 820}},
    {"id": "ORDERS-5183", "title": "Orders scenario 5183", "data": {"sku": "SKU5183", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5183@example.com", "threshold": 830}},
    {"id": "ORDERS-5184", "title": "Orders scenario 5184", "data": {"sku": "SKU5184", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5184@example.com", "threshold": 840}},
    {"id": "ORDERS-5185", "title": "Orders scenario 5185", "data": {"sku": "SKU5185", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5185@example.com", "threshold": 850}},
    {"id": "ORDERS-5186", "title": "Orders scenario 5186", "data": {"sku": "SKU5186", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5186@example.com", "threshold": 860}},
    {"id": "ORDERS-5187", "title": "Orders scenario 5187", "data": {"sku": "SKU5187", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5187@example.com", "threshold": 870}},
    {"id": "ORDERS-5188", "title": "Orders scenario 5188", "data": {"sku": "SKU5188", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5188@example.com", "threshold": 880}},
    {"id": "ORDERS-5189", "title": "Orders scenario 5189", "data": {"sku": "SKU5189", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5189@example.com", "threshold": 890}},
    {"id": "ORDERS-5190", "title": "Orders scenario 5190", "data": {"sku": "SKU5190", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5190@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
