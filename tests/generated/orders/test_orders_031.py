import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1821", "title": "Orders scenario 1821", "data": {"sku": "SKU1821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1821@example.com", "threshold": 210}},
    {"id": "ORDERS-1822", "title": "Orders scenario 1822", "data": {"sku": "SKU1822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1822@example.com", "threshold": 220}},
    {"id": "ORDERS-1823", "title": "Orders scenario 1823", "data": {"sku": "SKU1823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1823@example.com", "threshold": 230}},
    {"id": "ORDERS-1824", "title": "Orders scenario 1824", "data": {"sku": "SKU1824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1824@example.com", "threshold": 240}},
    {"id": "ORDERS-1825", "title": "Orders scenario 1825", "data": {"sku": "SKU1825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1825@example.com", "threshold": 250}},
    {"id": "ORDERS-1826", "title": "Orders scenario 1826", "data": {"sku": "SKU1826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1826@example.com", "threshold": 260}},
    {"id": "ORDERS-1827", "title": "Orders scenario 1827", "data": {"sku": "SKU1827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1827@example.com", "threshold": 270}},
    {"id": "ORDERS-1828", "title": "Orders scenario 1828", "data": {"sku": "SKU1828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1828@example.com", "threshold": 280}},
    {"id": "ORDERS-1829", "title": "Orders scenario 1829", "data": {"sku": "SKU1829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1829@example.com", "threshold": 290}},
    {"id": "ORDERS-1830", "title": "Orders scenario 1830", "data": {"sku": "SKU1830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1830@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
