import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8661", "title": "Orders scenario 8661", "data": {"sku": "SKU8661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8661@example.com", "threshold": 610}},
    {"id": "ORDERS-8662", "title": "Orders scenario 8662", "data": {"sku": "SKU8662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8662@example.com", "threshold": 620}},
    {"id": "ORDERS-8663", "title": "Orders scenario 8663", "data": {"sku": "SKU8663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8663@example.com", "threshold": 630}},
    {"id": "ORDERS-8664", "title": "Orders scenario 8664", "data": {"sku": "SKU8664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8664@example.com", "threshold": 640}},
    {"id": "ORDERS-8665", "title": "Orders scenario 8665", "data": {"sku": "SKU8665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8665@example.com", "threshold": 650}},
    {"id": "ORDERS-8666", "title": "Orders scenario 8666", "data": {"sku": "SKU8666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8666@example.com", "threshold": 660}},
    {"id": "ORDERS-8667", "title": "Orders scenario 8667", "data": {"sku": "SKU8667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8667@example.com", "threshold": 670}},
    {"id": "ORDERS-8668", "title": "Orders scenario 8668", "data": {"sku": "SKU8668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8668@example.com", "threshold": 680}},
    {"id": "ORDERS-8669", "title": "Orders scenario 8669", "data": {"sku": "SKU8669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8669@example.com", "threshold": 690}},
    {"id": "ORDERS-8670", "title": "Orders scenario 8670", "data": {"sku": "SKU8670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8670@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
