import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0201", "title": "Orders scenario 201", "data": {"sku": "SKU201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user201@example.com", "threshold": 10}},
    {"id": "ORDERS-0202", "title": "Orders scenario 202", "data": {"sku": "SKU202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user202@example.com", "threshold": 20}},
    {"id": "ORDERS-0203", "title": "Orders scenario 203", "data": {"sku": "SKU203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user203@example.com", "threshold": 30}},
    {"id": "ORDERS-0204", "title": "Orders scenario 204", "data": {"sku": "SKU204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user204@example.com", "threshold": 40}},
    {"id": "ORDERS-0205", "title": "Orders scenario 205", "data": {"sku": "SKU205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user205@example.com", "threshold": 50}},
    {"id": "ORDERS-0206", "title": "Orders scenario 206", "data": {"sku": "SKU206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user206@example.com", "threshold": 60}},
    {"id": "ORDERS-0207", "title": "Orders scenario 207", "data": {"sku": "SKU207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user207@example.com", "threshold": 70}},
    {"id": "ORDERS-0208", "title": "Orders scenario 208", "data": {"sku": "SKU208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user208@example.com", "threshold": 80}},
    {"id": "ORDERS-0209", "title": "Orders scenario 209", "data": {"sku": "SKU209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user209@example.com", "threshold": 90}},
    {"id": "ORDERS-0210", "title": "Orders scenario 210", "data": {"sku": "SKU210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user210@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
