import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5421", "title": "Orders scenario 5421", "data": {"sku": "SKU5421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5421@example.com", "threshold": 210}},
    {"id": "ORDERS-5422", "title": "Orders scenario 5422", "data": {"sku": "SKU5422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5422@example.com", "threshold": 220}},
    {"id": "ORDERS-5423", "title": "Orders scenario 5423", "data": {"sku": "SKU5423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5423@example.com", "threshold": 230}},
    {"id": "ORDERS-5424", "title": "Orders scenario 5424", "data": {"sku": "SKU5424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5424@example.com", "threshold": 240}},
    {"id": "ORDERS-5425", "title": "Orders scenario 5425", "data": {"sku": "SKU5425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5425@example.com", "threshold": 250}},
    {"id": "ORDERS-5426", "title": "Orders scenario 5426", "data": {"sku": "SKU5426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5426@example.com", "threshold": 260}},
    {"id": "ORDERS-5427", "title": "Orders scenario 5427", "data": {"sku": "SKU5427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5427@example.com", "threshold": 270}},
    {"id": "ORDERS-5428", "title": "Orders scenario 5428", "data": {"sku": "SKU5428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5428@example.com", "threshold": 280}},
    {"id": "ORDERS-5429", "title": "Orders scenario 5429", "data": {"sku": "SKU5429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5429@example.com", "threshold": 290}},
    {"id": "ORDERS-5430", "title": "Orders scenario 5430", "data": {"sku": "SKU5430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5430@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
