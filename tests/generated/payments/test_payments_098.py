import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5851", "title": "Payments scenario 5851", "data": {"sku": "SKU5851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5851@example.com", "threshold": 510}},
    {"id": "PAYMENTS-5852", "title": "Payments scenario 5852", "data": {"sku": "SKU5852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5852@example.com", "threshold": 520}},
    {"id": "PAYMENTS-5853", "title": "Payments scenario 5853", "data": {"sku": "SKU5853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5853@example.com", "threshold": 530}},
    {"id": "PAYMENTS-5854", "title": "Payments scenario 5854", "data": {"sku": "SKU5854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5854@example.com", "threshold": 540}},
    {"id": "PAYMENTS-5855", "title": "Payments scenario 5855", "data": {"sku": "SKU5855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5855@example.com", "threshold": 550}},
    {"id": "PAYMENTS-5856", "title": "Payments scenario 5856", "data": {"sku": "SKU5856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5856@example.com", "threshold": 560}},
    {"id": "PAYMENTS-5857", "title": "Payments scenario 5857", "data": {"sku": "SKU5857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5857@example.com", "threshold": 570}},
    {"id": "PAYMENTS-5858", "title": "Payments scenario 5858", "data": {"sku": "SKU5858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5858@example.com", "threshold": 580}},
    {"id": "PAYMENTS-5859", "title": "Payments scenario 5859", "data": {"sku": "SKU5859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5859@example.com", "threshold": 590}},
    {"id": "PAYMENTS-5860", "title": "Payments scenario 5860", "data": {"sku": "SKU5860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5860@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
