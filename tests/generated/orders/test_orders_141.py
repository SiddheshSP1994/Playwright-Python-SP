import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8421", "title": "Orders scenario 8421", "data": {"sku": "SKU8421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8421@example.com", "threshold": 210}},
    {"id": "ORDERS-8422", "title": "Orders scenario 8422", "data": {"sku": "SKU8422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8422@example.com", "threshold": 220}},
    {"id": "ORDERS-8423", "title": "Orders scenario 8423", "data": {"sku": "SKU8423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8423@example.com", "threshold": 230}},
    {"id": "ORDERS-8424", "title": "Orders scenario 8424", "data": {"sku": "SKU8424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8424@example.com", "threshold": 240}},
    {"id": "ORDERS-8425", "title": "Orders scenario 8425", "data": {"sku": "SKU8425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8425@example.com", "threshold": 250}},
    {"id": "ORDERS-8426", "title": "Orders scenario 8426", "data": {"sku": "SKU8426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8426@example.com", "threshold": 260}},
    {"id": "ORDERS-8427", "title": "Orders scenario 8427", "data": {"sku": "SKU8427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8427@example.com", "threshold": 270}},
    {"id": "ORDERS-8428", "title": "Orders scenario 8428", "data": {"sku": "SKU8428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8428@example.com", "threshold": 280}},
    {"id": "ORDERS-8429", "title": "Orders scenario 8429", "data": {"sku": "SKU8429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8429@example.com", "threshold": 290}},
    {"id": "ORDERS-8430", "title": "Orders scenario 8430", "data": {"sku": "SKU8430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8430@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
