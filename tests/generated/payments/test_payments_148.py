import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8851", "title": "Payments scenario 8851", "data": {"sku": "SKU8851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8851@example.com", "threshold": 510}},
    {"id": "PAYMENTS-8852", "title": "Payments scenario 8852", "data": {"sku": "SKU8852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8852@example.com", "threshold": 520}},
    {"id": "PAYMENTS-8853", "title": "Payments scenario 8853", "data": {"sku": "SKU8853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8853@example.com", "threshold": 530}},
    {"id": "PAYMENTS-8854", "title": "Payments scenario 8854", "data": {"sku": "SKU8854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8854@example.com", "threshold": 540}},
    {"id": "PAYMENTS-8855", "title": "Payments scenario 8855", "data": {"sku": "SKU8855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8855@example.com", "threshold": 550}},
    {"id": "PAYMENTS-8856", "title": "Payments scenario 8856", "data": {"sku": "SKU8856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8856@example.com", "threshold": 560}},
    {"id": "PAYMENTS-8857", "title": "Payments scenario 8857", "data": {"sku": "SKU8857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8857@example.com", "threshold": 570}},
    {"id": "PAYMENTS-8858", "title": "Payments scenario 8858", "data": {"sku": "SKU8858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8858@example.com", "threshold": 580}},
    {"id": "PAYMENTS-8859", "title": "Payments scenario 8859", "data": {"sku": "SKU8859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8859@example.com", "threshold": 590}},
    {"id": "PAYMENTS-8860", "title": "Payments scenario 8860", "data": {"sku": "SKU8860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8860@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
