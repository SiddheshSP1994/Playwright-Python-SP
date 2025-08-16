import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4761", "title": "Orders scenario 4761", "data": {"sku": "SKU4761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4761@example.com", "threshold": 610}},
    {"id": "ORDERS-4762", "title": "Orders scenario 4762", "data": {"sku": "SKU4762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4762@example.com", "threshold": 620}},
    {"id": "ORDERS-4763", "title": "Orders scenario 4763", "data": {"sku": "SKU4763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4763@example.com", "threshold": 630}},
    {"id": "ORDERS-4764", "title": "Orders scenario 4764", "data": {"sku": "SKU4764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4764@example.com", "threshold": 640}},
    {"id": "ORDERS-4765", "title": "Orders scenario 4765", "data": {"sku": "SKU4765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4765@example.com", "threshold": 650}},
    {"id": "ORDERS-4766", "title": "Orders scenario 4766", "data": {"sku": "SKU4766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4766@example.com", "threshold": 660}},
    {"id": "ORDERS-4767", "title": "Orders scenario 4767", "data": {"sku": "SKU4767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4767@example.com", "threshold": 670}},
    {"id": "ORDERS-4768", "title": "Orders scenario 4768", "data": {"sku": "SKU4768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4768@example.com", "threshold": 680}},
    {"id": "ORDERS-4769", "title": "Orders scenario 4769", "data": {"sku": "SKU4769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4769@example.com", "threshold": 690}},
    {"id": "ORDERS-4770", "title": "Orders scenario 4770", "data": {"sku": "SKU4770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4770@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
