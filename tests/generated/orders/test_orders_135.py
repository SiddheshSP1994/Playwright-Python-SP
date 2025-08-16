import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8061", "title": "Orders scenario 8061", "data": {"sku": "SKU8061", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8061@example.com", "threshold": 610}},
    {"id": "ORDERS-8062", "title": "Orders scenario 8062", "data": {"sku": "SKU8062", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8062@example.com", "threshold": 620}},
    {"id": "ORDERS-8063", "title": "Orders scenario 8063", "data": {"sku": "SKU8063", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8063@example.com", "threshold": 630}},
    {"id": "ORDERS-8064", "title": "Orders scenario 8064", "data": {"sku": "SKU8064", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8064@example.com", "threshold": 640}},
    {"id": "ORDERS-8065", "title": "Orders scenario 8065", "data": {"sku": "SKU8065", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8065@example.com", "threshold": 650}},
    {"id": "ORDERS-8066", "title": "Orders scenario 8066", "data": {"sku": "SKU8066", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8066@example.com", "threshold": 660}},
    {"id": "ORDERS-8067", "title": "Orders scenario 8067", "data": {"sku": "SKU8067", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8067@example.com", "threshold": 670}},
    {"id": "ORDERS-8068", "title": "Orders scenario 8068", "data": {"sku": "SKU8068", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8068@example.com", "threshold": 680}},
    {"id": "ORDERS-8069", "title": "Orders scenario 8069", "data": {"sku": "SKU8069", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8069@example.com", "threshold": 690}},
    {"id": "ORDERS-8070", "title": "Orders scenario 8070", "data": {"sku": "SKU8070", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8070@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
