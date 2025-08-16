import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5001", "title": "Orders scenario 5001", "data": {"sku": "SKU5001", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5001@example.com", "threshold": 10}},
    {"id": "ORDERS-5002", "title": "Orders scenario 5002", "data": {"sku": "SKU5002", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5002@example.com", "threshold": 20}},
    {"id": "ORDERS-5003", "title": "Orders scenario 5003", "data": {"sku": "SKU5003", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5003@example.com", "threshold": 30}},
    {"id": "ORDERS-5004", "title": "Orders scenario 5004", "data": {"sku": "SKU5004", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5004@example.com", "threshold": 40}},
    {"id": "ORDERS-5005", "title": "Orders scenario 5005", "data": {"sku": "SKU5005", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5005@example.com", "threshold": 50}},
    {"id": "ORDERS-5006", "title": "Orders scenario 5006", "data": {"sku": "SKU5006", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5006@example.com", "threshold": 60}},
    {"id": "ORDERS-5007", "title": "Orders scenario 5007", "data": {"sku": "SKU5007", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5007@example.com", "threshold": 70}},
    {"id": "ORDERS-5008", "title": "Orders scenario 5008", "data": {"sku": "SKU5008", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5008@example.com", "threshold": 80}},
    {"id": "ORDERS-5009", "title": "Orders scenario 5009", "data": {"sku": "SKU5009", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5009@example.com", "threshold": 90}},
    {"id": "ORDERS-5010", "title": "Orders scenario 5010", "data": {"sku": "SKU5010", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5010@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
