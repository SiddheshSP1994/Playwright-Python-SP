import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8601", "title": "Orders scenario 8601", "data": {"sku": "SKU8601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8601@example.com", "threshold": 10}},
    {"id": "ORDERS-8602", "title": "Orders scenario 8602", "data": {"sku": "SKU8602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8602@example.com", "threshold": 20}},
    {"id": "ORDERS-8603", "title": "Orders scenario 8603", "data": {"sku": "SKU8603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8603@example.com", "threshold": 30}},
    {"id": "ORDERS-8604", "title": "Orders scenario 8604", "data": {"sku": "SKU8604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8604@example.com", "threshold": 40}},
    {"id": "ORDERS-8605", "title": "Orders scenario 8605", "data": {"sku": "SKU8605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8605@example.com", "threshold": 50}},
    {"id": "ORDERS-8606", "title": "Orders scenario 8606", "data": {"sku": "SKU8606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8606@example.com", "threshold": 60}},
    {"id": "ORDERS-8607", "title": "Orders scenario 8607", "data": {"sku": "SKU8607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8607@example.com", "threshold": 70}},
    {"id": "ORDERS-8608", "title": "Orders scenario 8608", "data": {"sku": "SKU8608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8608@example.com", "threshold": 80}},
    {"id": "ORDERS-8609", "title": "Orders scenario 8609", "data": {"sku": "SKU8609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8609@example.com", "threshold": 90}},
    {"id": "ORDERS-8610", "title": "Orders scenario 8610", "data": {"sku": "SKU8610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8610@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
