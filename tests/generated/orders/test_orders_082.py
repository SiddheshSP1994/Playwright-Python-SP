import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4881", "title": "Orders scenario 4881", "data": {"sku": "SKU4881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4881@example.com", "threshold": 810}},
    {"id": "ORDERS-4882", "title": "Orders scenario 4882", "data": {"sku": "SKU4882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4882@example.com", "threshold": 820}},
    {"id": "ORDERS-4883", "title": "Orders scenario 4883", "data": {"sku": "SKU4883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4883@example.com", "threshold": 830}},
    {"id": "ORDERS-4884", "title": "Orders scenario 4884", "data": {"sku": "SKU4884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4884@example.com", "threshold": 840}},
    {"id": "ORDERS-4885", "title": "Orders scenario 4885", "data": {"sku": "SKU4885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4885@example.com", "threshold": 850}},
    {"id": "ORDERS-4886", "title": "Orders scenario 4886", "data": {"sku": "SKU4886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4886@example.com", "threshold": 860}},
    {"id": "ORDERS-4887", "title": "Orders scenario 4887", "data": {"sku": "SKU4887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4887@example.com", "threshold": 870}},
    {"id": "ORDERS-4888", "title": "Orders scenario 4888", "data": {"sku": "SKU4888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4888@example.com", "threshold": 880}},
    {"id": "ORDERS-4889", "title": "Orders scenario 4889", "data": {"sku": "SKU4889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4889@example.com", "threshold": 890}},
    {"id": "ORDERS-4890", "title": "Orders scenario 4890", "data": {"sku": "SKU4890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4890@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
