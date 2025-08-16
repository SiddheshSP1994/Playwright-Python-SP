import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8001", "title": "Orders scenario 8001", "data": {"sku": "SKU8001", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8001@example.com", "threshold": 10}},
    {"id": "ORDERS-8002", "title": "Orders scenario 8002", "data": {"sku": "SKU8002", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8002@example.com", "threshold": 20}},
    {"id": "ORDERS-8003", "title": "Orders scenario 8003", "data": {"sku": "SKU8003", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8003@example.com", "threshold": 30}},
    {"id": "ORDERS-8004", "title": "Orders scenario 8004", "data": {"sku": "SKU8004", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8004@example.com", "threshold": 40}},
    {"id": "ORDERS-8005", "title": "Orders scenario 8005", "data": {"sku": "SKU8005", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8005@example.com", "threshold": 50}},
    {"id": "ORDERS-8006", "title": "Orders scenario 8006", "data": {"sku": "SKU8006", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8006@example.com", "threshold": 60}},
    {"id": "ORDERS-8007", "title": "Orders scenario 8007", "data": {"sku": "SKU8007", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8007@example.com", "threshold": 70}},
    {"id": "ORDERS-8008", "title": "Orders scenario 8008", "data": {"sku": "SKU8008", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8008@example.com", "threshold": 80}},
    {"id": "ORDERS-8009", "title": "Orders scenario 8009", "data": {"sku": "SKU8009", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8009@example.com", "threshold": 90}},
    {"id": "ORDERS-8010", "title": "Orders scenario 8010", "data": {"sku": "SKU8010", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8010@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
