import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5661", "title": "Orders scenario 5661", "data": {"sku": "SKU5661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5661@example.com", "threshold": 610}},
    {"id": "ORDERS-5662", "title": "Orders scenario 5662", "data": {"sku": "SKU5662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5662@example.com", "threshold": 620}},
    {"id": "ORDERS-5663", "title": "Orders scenario 5663", "data": {"sku": "SKU5663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5663@example.com", "threshold": 630}},
    {"id": "ORDERS-5664", "title": "Orders scenario 5664", "data": {"sku": "SKU5664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5664@example.com", "threshold": 640}},
    {"id": "ORDERS-5665", "title": "Orders scenario 5665", "data": {"sku": "SKU5665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5665@example.com", "threshold": 650}},
    {"id": "ORDERS-5666", "title": "Orders scenario 5666", "data": {"sku": "SKU5666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5666@example.com", "threshold": 660}},
    {"id": "ORDERS-5667", "title": "Orders scenario 5667", "data": {"sku": "SKU5667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5667@example.com", "threshold": 670}},
    {"id": "ORDERS-5668", "title": "Orders scenario 5668", "data": {"sku": "SKU5668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5668@example.com", "threshold": 680}},
    {"id": "ORDERS-5669", "title": "Orders scenario 5669", "data": {"sku": "SKU5669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5669@example.com", "threshold": 690}},
    {"id": "ORDERS-5670", "title": "Orders scenario 5670", "data": {"sku": "SKU5670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5670@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
