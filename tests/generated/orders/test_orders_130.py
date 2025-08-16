import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7761", "title": "Orders scenario 7761", "data": {"sku": "SKU7761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7761@example.com", "threshold": 610}},
    {"id": "ORDERS-7762", "title": "Orders scenario 7762", "data": {"sku": "SKU7762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7762@example.com", "threshold": 620}},
    {"id": "ORDERS-7763", "title": "Orders scenario 7763", "data": {"sku": "SKU7763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7763@example.com", "threshold": 630}},
    {"id": "ORDERS-7764", "title": "Orders scenario 7764", "data": {"sku": "SKU7764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7764@example.com", "threshold": 640}},
    {"id": "ORDERS-7765", "title": "Orders scenario 7765", "data": {"sku": "SKU7765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7765@example.com", "threshold": 650}},
    {"id": "ORDERS-7766", "title": "Orders scenario 7766", "data": {"sku": "SKU7766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7766@example.com", "threshold": 660}},
    {"id": "ORDERS-7767", "title": "Orders scenario 7767", "data": {"sku": "SKU7767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7767@example.com", "threshold": 670}},
    {"id": "ORDERS-7768", "title": "Orders scenario 7768", "data": {"sku": "SKU7768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7768@example.com", "threshold": 680}},
    {"id": "ORDERS-7769", "title": "Orders scenario 7769", "data": {"sku": "SKU7769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7769@example.com", "threshold": 690}},
    {"id": "ORDERS-7770", "title": "Orders scenario 7770", "data": {"sku": "SKU7770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7770@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
