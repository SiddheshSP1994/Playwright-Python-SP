import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9681", "title": "Orders scenario 9681", "data": {"sku": "SKU9681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9681@example.com", "threshold": 810}},
    {"id": "ORDERS-9682", "title": "Orders scenario 9682", "data": {"sku": "SKU9682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9682@example.com", "threshold": 820}},
    {"id": "ORDERS-9683", "title": "Orders scenario 9683", "data": {"sku": "SKU9683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9683@example.com", "threshold": 830}},
    {"id": "ORDERS-9684", "title": "Orders scenario 9684", "data": {"sku": "SKU9684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9684@example.com", "threshold": 840}},
    {"id": "ORDERS-9685", "title": "Orders scenario 9685", "data": {"sku": "SKU9685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9685@example.com", "threshold": 850}},
    {"id": "ORDERS-9686", "title": "Orders scenario 9686", "data": {"sku": "SKU9686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9686@example.com", "threshold": 860}},
    {"id": "ORDERS-9687", "title": "Orders scenario 9687", "data": {"sku": "SKU9687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9687@example.com", "threshold": 870}},
    {"id": "ORDERS-9688", "title": "Orders scenario 9688", "data": {"sku": "SKU9688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9688@example.com", "threshold": 880}},
    {"id": "ORDERS-9689", "title": "Orders scenario 9689", "data": {"sku": "SKU9689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9689@example.com", "threshold": 890}},
    {"id": "ORDERS-9690", "title": "Orders scenario 9690", "data": {"sku": "SKU9690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9690@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
