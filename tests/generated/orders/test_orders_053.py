import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3141", "title": "Orders scenario 3141", "data": {"sku": "SKU3141", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3141@example.com", "threshold": 410}},
    {"id": "ORDERS-3142", "title": "Orders scenario 3142", "data": {"sku": "SKU3142", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3142@example.com", "threshold": 420}},
    {"id": "ORDERS-3143", "title": "Orders scenario 3143", "data": {"sku": "SKU3143", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3143@example.com", "threshold": 430}},
    {"id": "ORDERS-3144", "title": "Orders scenario 3144", "data": {"sku": "SKU3144", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3144@example.com", "threshold": 440}},
    {"id": "ORDERS-3145", "title": "Orders scenario 3145", "data": {"sku": "SKU3145", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3145@example.com", "threshold": 450}},
    {"id": "ORDERS-3146", "title": "Orders scenario 3146", "data": {"sku": "SKU3146", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3146@example.com", "threshold": 460}},
    {"id": "ORDERS-3147", "title": "Orders scenario 3147", "data": {"sku": "SKU3147", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3147@example.com", "threshold": 470}},
    {"id": "ORDERS-3148", "title": "Orders scenario 3148", "data": {"sku": "SKU3148", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3148@example.com", "threshold": 480}},
    {"id": "ORDERS-3149", "title": "Orders scenario 3149", "data": {"sku": "SKU3149", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3149@example.com", "threshold": 490}},
    {"id": "ORDERS-3150", "title": "Orders scenario 3150", "data": {"sku": "SKU3150", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3150@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
