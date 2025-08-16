import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3321", "title": "Orders scenario 3321", "data": {"sku": "SKU3321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3321@example.com", "threshold": 210}},
    {"id": "ORDERS-3322", "title": "Orders scenario 3322", "data": {"sku": "SKU3322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3322@example.com", "threshold": 220}},
    {"id": "ORDERS-3323", "title": "Orders scenario 3323", "data": {"sku": "SKU3323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3323@example.com", "threshold": 230}},
    {"id": "ORDERS-3324", "title": "Orders scenario 3324", "data": {"sku": "SKU3324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3324@example.com", "threshold": 240}},
    {"id": "ORDERS-3325", "title": "Orders scenario 3325", "data": {"sku": "SKU3325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3325@example.com", "threshold": 250}},
    {"id": "ORDERS-3326", "title": "Orders scenario 3326", "data": {"sku": "SKU3326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3326@example.com", "threshold": 260}},
    {"id": "ORDERS-3327", "title": "Orders scenario 3327", "data": {"sku": "SKU3327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3327@example.com", "threshold": 270}},
    {"id": "ORDERS-3328", "title": "Orders scenario 3328", "data": {"sku": "SKU3328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3328@example.com", "threshold": 280}},
    {"id": "ORDERS-3329", "title": "Orders scenario 3329", "data": {"sku": "SKU3329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3329@example.com", "threshold": 290}},
    {"id": "ORDERS-3330", "title": "Orders scenario 3330", "data": {"sku": "SKU3330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3330@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
