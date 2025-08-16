import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9921", "title": "Orders scenario 9921", "data": {"sku": "SKU9921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9921@example.com", "threshold": 210}},
    {"id": "ORDERS-9922", "title": "Orders scenario 9922", "data": {"sku": "SKU9922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9922@example.com", "threshold": 220}},
    {"id": "ORDERS-9923", "title": "Orders scenario 9923", "data": {"sku": "SKU9923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9923@example.com", "threshold": 230}},
    {"id": "ORDERS-9924", "title": "Orders scenario 9924", "data": {"sku": "SKU9924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9924@example.com", "threshold": 240}},
    {"id": "ORDERS-9925", "title": "Orders scenario 9925", "data": {"sku": "SKU9925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9925@example.com", "threshold": 250}},
    {"id": "ORDERS-9926", "title": "Orders scenario 9926", "data": {"sku": "SKU9926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9926@example.com", "threshold": 260}},
    {"id": "ORDERS-9927", "title": "Orders scenario 9927", "data": {"sku": "SKU9927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9927@example.com", "threshold": 270}},
    {"id": "ORDERS-9928", "title": "Orders scenario 9928", "data": {"sku": "SKU9928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9928@example.com", "threshold": 280}},
    {"id": "ORDERS-9929", "title": "Orders scenario 9929", "data": {"sku": "SKU9929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9929@example.com", "threshold": 290}},
    {"id": "ORDERS-9930", "title": "Orders scenario 9930", "data": {"sku": "SKU9930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9930@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
