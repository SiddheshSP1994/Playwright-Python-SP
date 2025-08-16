import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4641", "title": "Orders scenario 4641", "data": {"sku": "SKU4641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4641@example.com", "threshold": 410}},
    {"id": "ORDERS-4642", "title": "Orders scenario 4642", "data": {"sku": "SKU4642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4642@example.com", "threshold": 420}},
    {"id": "ORDERS-4643", "title": "Orders scenario 4643", "data": {"sku": "SKU4643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4643@example.com", "threshold": 430}},
    {"id": "ORDERS-4644", "title": "Orders scenario 4644", "data": {"sku": "SKU4644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4644@example.com", "threshold": 440}},
    {"id": "ORDERS-4645", "title": "Orders scenario 4645", "data": {"sku": "SKU4645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4645@example.com", "threshold": 450}},
    {"id": "ORDERS-4646", "title": "Orders scenario 4646", "data": {"sku": "SKU4646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4646@example.com", "threshold": 460}},
    {"id": "ORDERS-4647", "title": "Orders scenario 4647", "data": {"sku": "SKU4647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4647@example.com", "threshold": 470}},
    {"id": "ORDERS-4648", "title": "Orders scenario 4648", "data": {"sku": "SKU4648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4648@example.com", "threshold": 480}},
    {"id": "ORDERS-4649", "title": "Orders scenario 4649", "data": {"sku": "SKU4649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4649@example.com", "threshold": 490}},
    {"id": "ORDERS-4650", "title": "Orders scenario 4650", "data": {"sku": "SKU4650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4650@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
