import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1651", "title": "Payments scenario 1651", "data": {"sku": "SKU1651", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1651@example.com", "threshold": 510}},
    {"id": "PAYMENTS-1652", "title": "Payments scenario 1652", "data": {"sku": "SKU1652", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1652@example.com", "threshold": 520}},
    {"id": "PAYMENTS-1653", "title": "Payments scenario 1653", "data": {"sku": "SKU1653", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1653@example.com", "threshold": 530}},
    {"id": "PAYMENTS-1654", "title": "Payments scenario 1654", "data": {"sku": "SKU1654", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1654@example.com", "threshold": 540}},
    {"id": "PAYMENTS-1655", "title": "Payments scenario 1655", "data": {"sku": "SKU1655", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1655@example.com", "threshold": 550}},
    {"id": "PAYMENTS-1656", "title": "Payments scenario 1656", "data": {"sku": "SKU1656", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1656@example.com", "threshold": 560}},
    {"id": "PAYMENTS-1657", "title": "Payments scenario 1657", "data": {"sku": "SKU1657", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1657@example.com", "threshold": 570}},
    {"id": "PAYMENTS-1658", "title": "Payments scenario 1658", "data": {"sku": "SKU1658", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1658@example.com", "threshold": 580}},
    {"id": "PAYMENTS-1659", "title": "Payments scenario 1659", "data": {"sku": "SKU1659", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1659@example.com", "threshold": 590}},
    {"id": "PAYMENTS-1660", "title": "Payments scenario 1660", "data": {"sku": "SKU1660", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1660@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
