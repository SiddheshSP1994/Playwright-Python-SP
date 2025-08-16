import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-6991", "title": "Payments scenario 6991", "data": {"sku": "SKU6991", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6991@example.com", "threshold": 910}},
    {"id": "PAYMENTS-6992", "title": "Payments scenario 6992", "data": {"sku": "SKU6992", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6992@example.com", "threshold": 920}},
    {"id": "PAYMENTS-6993", "title": "Payments scenario 6993", "data": {"sku": "SKU6993", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6993@example.com", "threshold": 930}},
    {"id": "PAYMENTS-6994", "title": "Payments scenario 6994", "data": {"sku": "SKU6994", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6994@example.com", "threshold": 940}},
    {"id": "PAYMENTS-6995", "title": "Payments scenario 6995", "data": {"sku": "SKU6995", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6995@example.com", "threshold": 950}},
    {"id": "PAYMENTS-6996", "title": "Payments scenario 6996", "data": {"sku": "SKU6996", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6996@example.com", "threshold": 960}},
    {"id": "PAYMENTS-6997", "title": "Payments scenario 6997", "data": {"sku": "SKU6997", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6997@example.com", "threshold": 970}},
    {"id": "PAYMENTS-6998", "title": "Payments scenario 6998", "data": {"sku": "SKU6998", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6998@example.com", "threshold": 980}},
    {"id": "PAYMENTS-6999", "title": "Payments scenario 6999", "data": {"sku": "SKU6999", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6999@example.com", "threshold": 990}},
    {"id": "PAYMENTS-7000", "title": "Payments scenario 7000", "data": {"sku": "SKU7000", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7000@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
