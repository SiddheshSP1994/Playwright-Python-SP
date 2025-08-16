import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7651", "title": "Payments scenario 7651", "data": {"sku": "SKU7651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7651@example.com", "threshold": 510}},
    {"id": "PAYMENTS-7652", "title": "Payments scenario 7652", "data": {"sku": "SKU7652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7652@example.com", "threshold": 520}},
    {"id": "PAYMENTS-7653", "title": "Payments scenario 7653", "data": {"sku": "SKU7653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7653@example.com", "threshold": 530}},
    {"id": "PAYMENTS-7654", "title": "Payments scenario 7654", "data": {"sku": "SKU7654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7654@example.com", "threshold": 540}},
    {"id": "PAYMENTS-7655", "title": "Payments scenario 7655", "data": {"sku": "SKU7655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7655@example.com", "threshold": 550}},
    {"id": "PAYMENTS-7656", "title": "Payments scenario 7656", "data": {"sku": "SKU7656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7656@example.com", "threshold": 560}},
    {"id": "PAYMENTS-7657", "title": "Payments scenario 7657", "data": {"sku": "SKU7657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7657@example.com", "threshold": 570}},
    {"id": "PAYMENTS-7658", "title": "Payments scenario 7658", "data": {"sku": "SKU7658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7658@example.com", "threshold": 580}},
    {"id": "PAYMENTS-7659", "title": "Payments scenario 7659", "data": {"sku": "SKU7659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7659@example.com", "threshold": 590}},
    {"id": "PAYMENTS-7660", "title": "Payments scenario 7660", "data": {"sku": "SKU7660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7660@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
