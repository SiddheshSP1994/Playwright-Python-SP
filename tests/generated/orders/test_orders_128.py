import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7641", "title": "Orders scenario 7641", "data": {"sku": "SKU7641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7641@example.com", "threshold": 410}},
    {"id": "ORDERS-7642", "title": "Orders scenario 7642", "data": {"sku": "SKU7642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7642@example.com", "threshold": 420}},
    {"id": "ORDERS-7643", "title": "Orders scenario 7643", "data": {"sku": "SKU7643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7643@example.com", "threshold": 430}},
    {"id": "ORDERS-7644", "title": "Orders scenario 7644", "data": {"sku": "SKU7644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7644@example.com", "threshold": 440}},
    {"id": "ORDERS-7645", "title": "Orders scenario 7645", "data": {"sku": "SKU7645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7645@example.com", "threshold": 450}},
    {"id": "ORDERS-7646", "title": "Orders scenario 7646", "data": {"sku": "SKU7646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7646@example.com", "threshold": 460}},
    {"id": "ORDERS-7647", "title": "Orders scenario 7647", "data": {"sku": "SKU7647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7647@example.com", "threshold": 470}},
    {"id": "ORDERS-7648", "title": "Orders scenario 7648", "data": {"sku": "SKU7648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7648@example.com", "threshold": 480}},
    {"id": "ORDERS-7649", "title": "Orders scenario 7649", "data": {"sku": "SKU7649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7649@example.com", "threshold": 490}},
    {"id": "ORDERS-7650", "title": "Orders scenario 7650", "data": {"sku": "SKU7650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7650@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
