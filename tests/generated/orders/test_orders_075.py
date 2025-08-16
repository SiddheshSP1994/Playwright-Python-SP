import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4461", "title": "Orders scenario 4461", "data": {"sku": "SKU4461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4461@example.com", "threshold": 610}},
    {"id": "ORDERS-4462", "title": "Orders scenario 4462", "data": {"sku": "SKU4462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4462@example.com", "threshold": 620}},
    {"id": "ORDERS-4463", "title": "Orders scenario 4463", "data": {"sku": "SKU4463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4463@example.com", "threshold": 630}},
    {"id": "ORDERS-4464", "title": "Orders scenario 4464", "data": {"sku": "SKU4464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4464@example.com", "threshold": 640}},
    {"id": "ORDERS-4465", "title": "Orders scenario 4465", "data": {"sku": "SKU4465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4465@example.com", "threshold": 650}},
    {"id": "ORDERS-4466", "title": "Orders scenario 4466", "data": {"sku": "SKU4466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4466@example.com", "threshold": 660}},
    {"id": "ORDERS-4467", "title": "Orders scenario 4467", "data": {"sku": "SKU4467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4467@example.com", "threshold": 670}},
    {"id": "ORDERS-4468", "title": "Orders scenario 4468", "data": {"sku": "SKU4468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4468@example.com", "threshold": 680}},
    {"id": "ORDERS-4469", "title": "Orders scenario 4469", "data": {"sku": "SKU4469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4469@example.com", "threshold": 690}},
    {"id": "ORDERS-4470", "title": "Orders scenario 4470", "data": {"sku": "SKU4470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4470@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
