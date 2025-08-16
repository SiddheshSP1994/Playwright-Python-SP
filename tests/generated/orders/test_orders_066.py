import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3921", "title": "Orders scenario 3921", "data": {"sku": "SKU3921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3921@example.com", "threshold": 210}},
    {"id": "ORDERS-3922", "title": "Orders scenario 3922", "data": {"sku": "SKU3922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3922@example.com", "threshold": 220}},
    {"id": "ORDERS-3923", "title": "Orders scenario 3923", "data": {"sku": "SKU3923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3923@example.com", "threshold": 230}},
    {"id": "ORDERS-3924", "title": "Orders scenario 3924", "data": {"sku": "SKU3924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3924@example.com", "threshold": 240}},
    {"id": "ORDERS-3925", "title": "Orders scenario 3925", "data": {"sku": "SKU3925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3925@example.com", "threshold": 250}},
    {"id": "ORDERS-3926", "title": "Orders scenario 3926", "data": {"sku": "SKU3926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3926@example.com", "threshold": 260}},
    {"id": "ORDERS-3927", "title": "Orders scenario 3927", "data": {"sku": "SKU3927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3927@example.com", "threshold": 270}},
    {"id": "ORDERS-3928", "title": "Orders scenario 3928", "data": {"sku": "SKU3928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3928@example.com", "threshold": 280}},
    {"id": "ORDERS-3929", "title": "Orders scenario 3929", "data": {"sku": "SKU3929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3929@example.com", "threshold": 290}},
    {"id": "ORDERS-3930", "title": "Orders scenario 3930", "data": {"sku": "SKU3930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3930@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
