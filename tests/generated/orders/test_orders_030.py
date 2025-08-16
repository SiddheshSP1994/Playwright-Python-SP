import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1761", "title": "Orders scenario 1761", "data": {"sku": "SKU1761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1761@example.com", "threshold": 610}},
    {"id": "ORDERS-1762", "title": "Orders scenario 1762", "data": {"sku": "SKU1762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1762@example.com", "threshold": 620}},
    {"id": "ORDERS-1763", "title": "Orders scenario 1763", "data": {"sku": "SKU1763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1763@example.com", "threshold": 630}},
    {"id": "ORDERS-1764", "title": "Orders scenario 1764", "data": {"sku": "SKU1764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1764@example.com", "threshold": 640}},
    {"id": "ORDERS-1765", "title": "Orders scenario 1765", "data": {"sku": "SKU1765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1765@example.com", "threshold": 650}},
    {"id": "ORDERS-1766", "title": "Orders scenario 1766", "data": {"sku": "SKU1766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1766@example.com", "threshold": 660}},
    {"id": "ORDERS-1767", "title": "Orders scenario 1767", "data": {"sku": "SKU1767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1767@example.com", "threshold": 670}},
    {"id": "ORDERS-1768", "title": "Orders scenario 1768", "data": {"sku": "SKU1768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1768@example.com", "threshold": 680}},
    {"id": "ORDERS-1769", "title": "Orders scenario 1769", "data": {"sku": "SKU1769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1769@example.com", "threshold": 690}},
    {"id": "ORDERS-1770", "title": "Orders scenario 1770", "data": {"sku": "SKU1770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1770@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
