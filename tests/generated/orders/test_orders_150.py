import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8961", "title": "Orders scenario 8961", "data": {"sku": "SKU8961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8961@example.com", "threshold": 610}},
    {"id": "ORDERS-8962", "title": "Orders scenario 8962", "data": {"sku": "SKU8962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8962@example.com", "threshold": 620}},
    {"id": "ORDERS-8963", "title": "Orders scenario 8963", "data": {"sku": "SKU8963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8963@example.com", "threshold": 630}},
    {"id": "ORDERS-8964", "title": "Orders scenario 8964", "data": {"sku": "SKU8964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8964@example.com", "threshold": 640}},
    {"id": "ORDERS-8965", "title": "Orders scenario 8965", "data": {"sku": "SKU8965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8965@example.com", "threshold": 650}},
    {"id": "ORDERS-8966", "title": "Orders scenario 8966", "data": {"sku": "SKU8966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8966@example.com", "threshold": 660}},
    {"id": "ORDERS-8967", "title": "Orders scenario 8967", "data": {"sku": "SKU8967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8967@example.com", "threshold": 670}},
    {"id": "ORDERS-8968", "title": "Orders scenario 8968", "data": {"sku": "SKU8968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8968@example.com", "threshold": 680}},
    {"id": "ORDERS-8969", "title": "Orders scenario 8969", "data": {"sku": "SKU8969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8969@example.com", "threshold": 690}},
    {"id": "ORDERS-8970", "title": "Orders scenario 8970", "data": {"sku": "SKU8970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8970@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
