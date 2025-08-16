import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8971", "title": "Payments scenario 8971", "data": {"sku": "SKU8971", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8971@example.com", "threshold": 710}},
    {"id": "PAYMENTS-8972", "title": "Payments scenario 8972", "data": {"sku": "SKU8972", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8972@example.com", "threshold": 720}},
    {"id": "PAYMENTS-8973", "title": "Payments scenario 8973", "data": {"sku": "SKU8973", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8973@example.com", "threshold": 730}},
    {"id": "PAYMENTS-8974", "title": "Payments scenario 8974", "data": {"sku": "SKU8974", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8974@example.com", "threshold": 740}},
    {"id": "PAYMENTS-8975", "title": "Payments scenario 8975", "data": {"sku": "SKU8975", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8975@example.com", "threshold": 750}},
    {"id": "PAYMENTS-8976", "title": "Payments scenario 8976", "data": {"sku": "SKU8976", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8976@example.com", "threshold": 760}},
    {"id": "PAYMENTS-8977", "title": "Payments scenario 8977", "data": {"sku": "SKU8977", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8977@example.com", "threshold": 770}},
    {"id": "PAYMENTS-8978", "title": "Payments scenario 8978", "data": {"sku": "SKU8978", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8978@example.com", "threshold": 780}},
    {"id": "PAYMENTS-8979", "title": "Payments scenario 8979", "data": {"sku": "SKU8979", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8979@example.com", "threshold": 790}},
    {"id": "PAYMENTS-8980", "title": "Payments scenario 8980", "data": {"sku": "SKU8980", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8980@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
