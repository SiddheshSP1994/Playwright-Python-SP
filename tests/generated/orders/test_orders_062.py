import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3681", "title": "Orders scenario 3681", "data": {"sku": "SKU3681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3681@example.com", "threshold": 810}},
    {"id": "ORDERS-3682", "title": "Orders scenario 3682", "data": {"sku": "SKU3682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3682@example.com", "threshold": 820}},
    {"id": "ORDERS-3683", "title": "Orders scenario 3683", "data": {"sku": "SKU3683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3683@example.com", "threshold": 830}},
    {"id": "ORDERS-3684", "title": "Orders scenario 3684", "data": {"sku": "SKU3684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3684@example.com", "threshold": 840}},
    {"id": "ORDERS-3685", "title": "Orders scenario 3685", "data": {"sku": "SKU3685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3685@example.com", "threshold": 850}},
    {"id": "ORDERS-3686", "title": "Orders scenario 3686", "data": {"sku": "SKU3686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3686@example.com", "threshold": 860}},
    {"id": "ORDERS-3687", "title": "Orders scenario 3687", "data": {"sku": "SKU3687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3687@example.com", "threshold": 870}},
    {"id": "ORDERS-3688", "title": "Orders scenario 3688", "data": {"sku": "SKU3688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3688@example.com", "threshold": 880}},
    {"id": "ORDERS-3689", "title": "Orders scenario 3689", "data": {"sku": "SKU3689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3689@example.com", "threshold": 890}},
    {"id": "ORDERS-3690", "title": "Orders scenario 3690", "data": {"sku": "SKU3690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3690@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
