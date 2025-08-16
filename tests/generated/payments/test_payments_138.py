import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8251", "title": "Payments scenario 8251", "data": {"sku": "SKU8251", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8251@example.com", "threshold": 510}},
    {"id": "PAYMENTS-8252", "title": "Payments scenario 8252", "data": {"sku": "SKU8252", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8252@example.com", "threshold": 520}},
    {"id": "PAYMENTS-8253", "title": "Payments scenario 8253", "data": {"sku": "SKU8253", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8253@example.com", "threshold": 530}},
    {"id": "PAYMENTS-8254", "title": "Payments scenario 8254", "data": {"sku": "SKU8254", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8254@example.com", "threshold": 540}},
    {"id": "PAYMENTS-8255", "title": "Payments scenario 8255", "data": {"sku": "SKU8255", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8255@example.com", "threshold": 550}},
    {"id": "PAYMENTS-8256", "title": "Payments scenario 8256", "data": {"sku": "SKU8256", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8256@example.com", "threshold": 560}},
    {"id": "PAYMENTS-8257", "title": "Payments scenario 8257", "data": {"sku": "SKU8257", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8257@example.com", "threshold": 570}},
    {"id": "PAYMENTS-8258", "title": "Payments scenario 8258", "data": {"sku": "SKU8258", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8258@example.com", "threshold": 580}},
    {"id": "PAYMENTS-8259", "title": "Payments scenario 8259", "data": {"sku": "SKU8259", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8259@example.com", "threshold": 590}},
    {"id": "PAYMENTS-8260", "title": "Payments scenario 8260", "data": {"sku": "SKU8260", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8260@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
