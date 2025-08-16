import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6681", "title": "Orders scenario 6681", "data": {"sku": "SKU6681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6681@example.com", "threshold": 810}},
    {"id": "ORDERS-6682", "title": "Orders scenario 6682", "data": {"sku": "SKU6682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6682@example.com", "threshold": 820}},
    {"id": "ORDERS-6683", "title": "Orders scenario 6683", "data": {"sku": "SKU6683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6683@example.com", "threshold": 830}},
    {"id": "ORDERS-6684", "title": "Orders scenario 6684", "data": {"sku": "SKU6684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6684@example.com", "threshold": 840}},
    {"id": "ORDERS-6685", "title": "Orders scenario 6685", "data": {"sku": "SKU6685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6685@example.com", "threshold": 850}},
    {"id": "ORDERS-6686", "title": "Orders scenario 6686", "data": {"sku": "SKU6686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6686@example.com", "threshold": 860}},
    {"id": "ORDERS-6687", "title": "Orders scenario 6687", "data": {"sku": "SKU6687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6687@example.com", "threshold": 870}},
    {"id": "ORDERS-6688", "title": "Orders scenario 6688", "data": {"sku": "SKU6688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6688@example.com", "threshold": 880}},
    {"id": "ORDERS-6689", "title": "Orders scenario 6689", "data": {"sku": "SKU6689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6689@example.com", "threshold": 890}},
    {"id": "ORDERS-6690", "title": "Orders scenario 6690", "data": {"sku": "SKU6690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6690@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
