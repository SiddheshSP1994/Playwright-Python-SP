import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4821", "title": "Orders scenario 4821", "data": {"sku": "SKU4821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4821@example.com", "threshold": 210}},
    {"id": "ORDERS-4822", "title": "Orders scenario 4822", "data": {"sku": "SKU4822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4822@example.com", "threshold": 220}},
    {"id": "ORDERS-4823", "title": "Orders scenario 4823", "data": {"sku": "SKU4823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4823@example.com", "threshold": 230}},
    {"id": "ORDERS-4824", "title": "Orders scenario 4824", "data": {"sku": "SKU4824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4824@example.com", "threshold": 240}},
    {"id": "ORDERS-4825", "title": "Orders scenario 4825", "data": {"sku": "SKU4825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4825@example.com", "threshold": 250}},
    {"id": "ORDERS-4826", "title": "Orders scenario 4826", "data": {"sku": "SKU4826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4826@example.com", "threshold": 260}},
    {"id": "ORDERS-4827", "title": "Orders scenario 4827", "data": {"sku": "SKU4827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4827@example.com", "threshold": 270}},
    {"id": "ORDERS-4828", "title": "Orders scenario 4828", "data": {"sku": "SKU4828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4828@example.com", "threshold": 280}},
    {"id": "ORDERS-4829", "title": "Orders scenario 4829", "data": {"sku": "SKU4829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4829@example.com", "threshold": 290}},
    {"id": "ORDERS-4830", "title": "Orders scenario 4830", "data": {"sku": "SKU4830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4830@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
