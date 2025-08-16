import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9081", "title": "Orders scenario 9081", "data": {"sku": "SKU9081", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9081@example.com", "threshold": 810}},
    {"id": "ORDERS-9082", "title": "Orders scenario 9082", "data": {"sku": "SKU9082", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9082@example.com", "threshold": 820}},
    {"id": "ORDERS-9083", "title": "Orders scenario 9083", "data": {"sku": "SKU9083", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9083@example.com", "threshold": 830}},
    {"id": "ORDERS-9084", "title": "Orders scenario 9084", "data": {"sku": "SKU9084", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9084@example.com", "threshold": 840}},
    {"id": "ORDERS-9085", "title": "Orders scenario 9085", "data": {"sku": "SKU9085", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9085@example.com", "threshold": 850}},
    {"id": "ORDERS-9086", "title": "Orders scenario 9086", "data": {"sku": "SKU9086", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9086@example.com", "threshold": 860}},
    {"id": "ORDERS-9087", "title": "Orders scenario 9087", "data": {"sku": "SKU9087", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9087@example.com", "threshold": 870}},
    {"id": "ORDERS-9088", "title": "Orders scenario 9088", "data": {"sku": "SKU9088", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9088@example.com", "threshold": 880}},
    {"id": "ORDERS-9089", "title": "Orders scenario 9089", "data": {"sku": "SKU9089", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9089@example.com", "threshold": 890}},
    {"id": "ORDERS-9090", "title": "Orders scenario 9090", "data": {"sku": "SKU9090", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9090@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
