import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6921", "title": "Orders scenario 6921", "data": {"sku": "SKU6921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6921@example.com", "threshold": 210}},
    {"id": "ORDERS-6922", "title": "Orders scenario 6922", "data": {"sku": "SKU6922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6922@example.com", "threshold": 220}},
    {"id": "ORDERS-6923", "title": "Orders scenario 6923", "data": {"sku": "SKU6923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6923@example.com", "threshold": 230}},
    {"id": "ORDERS-6924", "title": "Orders scenario 6924", "data": {"sku": "SKU6924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6924@example.com", "threshold": 240}},
    {"id": "ORDERS-6925", "title": "Orders scenario 6925", "data": {"sku": "SKU6925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6925@example.com", "threshold": 250}},
    {"id": "ORDERS-6926", "title": "Orders scenario 6926", "data": {"sku": "SKU6926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6926@example.com", "threshold": 260}},
    {"id": "ORDERS-6927", "title": "Orders scenario 6927", "data": {"sku": "SKU6927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6927@example.com", "threshold": 270}},
    {"id": "ORDERS-6928", "title": "Orders scenario 6928", "data": {"sku": "SKU6928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6928@example.com", "threshold": 280}},
    {"id": "ORDERS-6929", "title": "Orders scenario 6929", "data": {"sku": "SKU6929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6929@example.com", "threshold": 290}},
    {"id": "ORDERS-6930", "title": "Orders scenario 6930", "data": {"sku": "SKU6930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6930@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
