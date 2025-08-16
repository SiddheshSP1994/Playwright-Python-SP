import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3201", "title": "Orders scenario 3201", "data": {"sku": "SKU3201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3201@example.com", "threshold": 10}},
    {"id": "ORDERS-3202", "title": "Orders scenario 3202", "data": {"sku": "SKU3202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3202@example.com", "threshold": 20}},
    {"id": "ORDERS-3203", "title": "Orders scenario 3203", "data": {"sku": "SKU3203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3203@example.com", "threshold": 30}},
    {"id": "ORDERS-3204", "title": "Orders scenario 3204", "data": {"sku": "SKU3204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3204@example.com", "threshold": 40}},
    {"id": "ORDERS-3205", "title": "Orders scenario 3205", "data": {"sku": "SKU3205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3205@example.com", "threshold": 50}},
    {"id": "ORDERS-3206", "title": "Orders scenario 3206", "data": {"sku": "SKU3206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3206@example.com", "threshold": 60}},
    {"id": "ORDERS-3207", "title": "Orders scenario 3207", "data": {"sku": "SKU3207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3207@example.com", "threshold": 70}},
    {"id": "ORDERS-3208", "title": "Orders scenario 3208", "data": {"sku": "SKU3208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3208@example.com", "threshold": 80}},
    {"id": "ORDERS-3209", "title": "Orders scenario 3209", "data": {"sku": "SKU3209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3209@example.com", "threshold": 90}},
    {"id": "ORDERS-3210", "title": "Orders scenario 3210", "data": {"sku": "SKU3210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3210@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
