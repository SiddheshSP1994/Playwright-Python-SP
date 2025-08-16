import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6081", "title": "Orders scenario 6081", "data": {"sku": "SKU6081", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6081@example.com", "threshold": 810}},
    {"id": "ORDERS-6082", "title": "Orders scenario 6082", "data": {"sku": "SKU6082", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6082@example.com", "threshold": 820}},
    {"id": "ORDERS-6083", "title": "Orders scenario 6083", "data": {"sku": "SKU6083", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6083@example.com", "threshold": 830}},
    {"id": "ORDERS-6084", "title": "Orders scenario 6084", "data": {"sku": "SKU6084", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6084@example.com", "threshold": 840}},
    {"id": "ORDERS-6085", "title": "Orders scenario 6085", "data": {"sku": "SKU6085", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6085@example.com", "threshold": 850}},
    {"id": "ORDERS-6086", "title": "Orders scenario 6086", "data": {"sku": "SKU6086", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6086@example.com", "threshold": 860}},
    {"id": "ORDERS-6087", "title": "Orders scenario 6087", "data": {"sku": "SKU6087", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6087@example.com", "threshold": 870}},
    {"id": "ORDERS-6088", "title": "Orders scenario 6088", "data": {"sku": "SKU6088", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6088@example.com", "threshold": 880}},
    {"id": "ORDERS-6089", "title": "Orders scenario 6089", "data": {"sku": "SKU6089", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6089@example.com", "threshold": 890}},
    {"id": "ORDERS-6090", "title": "Orders scenario 6090", "data": {"sku": "SKU6090", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6090@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
