import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4651", "title": "Payments scenario 4651", "data": {"sku": "SKU4651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4651@example.com", "threshold": 510}},
    {"id": "PAYMENTS-4652", "title": "Payments scenario 4652", "data": {"sku": "SKU4652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4652@example.com", "threshold": 520}},
    {"id": "PAYMENTS-4653", "title": "Payments scenario 4653", "data": {"sku": "SKU4653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4653@example.com", "threshold": 530}},
    {"id": "PAYMENTS-4654", "title": "Payments scenario 4654", "data": {"sku": "SKU4654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4654@example.com", "threshold": 540}},
    {"id": "PAYMENTS-4655", "title": "Payments scenario 4655", "data": {"sku": "SKU4655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4655@example.com", "threshold": 550}},
    {"id": "PAYMENTS-4656", "title": "Payments scenario 4656", "data": {"sku": "SKU4656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4656@example.com", "threshold": 560}},
    {"id": "PAYMENTS-4657", "title": "Payments scenario 4657", "data": {"sku": "SKU4657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4657@example.com", "threshold": 570}},
    {"id": "PAYMENTS-4658", "title": "Payments scenario 4658", "data": {"sku": "SKU4658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4658@example.com", "threshold": 580}},
    {"id": "PAYMENTS-4659", "title": "Payments scenario 4659", "data": {"sku": "SKU4659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4659@example.com", "threshold": 590}},
    {"id": "PAYMENTS-4660", "title": "Payments scenario 4660", "data": {"sku": "SKU4660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4660@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
