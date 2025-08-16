import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1881", "title": "Orders scenario 1881", "data": {"sku": "SKU1881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1881@example.com", "threshold": 810}},
    {"id": "ORDERS-1882", "title": "Orders scenario 1882", "data": {"sku": "SKU1882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1882@example.com", "threshold": 820}},
    {"id": "ORDERS-1883", "title": "Orders scenario 1883", "data": {"sku": "SKU1883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1883@example.com", "threshold": 830}},
    {"id": "ORDERS-1884", "title": "Orders scenario 1884", "data": {"sku": "SKU1884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1884@example.com", "threshold": 840}},
    {"id": "ORDERS-1885", "title": "Orders scenario 1885", "data": {"sku": "SKU1885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1885@example.com", "threshold": 850}},
    {"id": "ORDERS-1886", "title": "Orders scenario 1886", "data": {"sku": "SKU1886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1886@example.com", "threshold": 860}},
    {"id": "ORDERS-1887", "title": "Orders scenario 1887", "data": {"sku": "SKU1887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1887@example.com", "threshold": 870}},
    {"id": "ORDERS-1888", "title": "Orders scenario 1888", "data": {"sku": "SKU1888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1888@example.com", "threshold": 880}},
    {"id": "ORDERS-1889", "title": "Orders scenario 1889", "data": {"sku": "SKU1889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1889@example.com", "threshold": 890}},
    {"id": "ORDERS-1890", "title": "Orders scenario 1890", "data": {"sku": "SKU1890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1890@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
