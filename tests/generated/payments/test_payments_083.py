import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4951", "title": "Payments scenario 4951", "data": {"sku": "SKU4951", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4951@example.com", "threshold": 510}},
    {"id": "PAYMENTS-4952", "title": "Payments scenario 4952", "data": {"sku": "SKU4952", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4952@example.com", "threshold": 520}},
    {"id": "PAYMENTS-4953", "title": "Payments scenario 4953", "data": {"sku": "SKU4953", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4953@example.com", "threshold": 530}},
    {"id": "PAYMENTS-4954", "title": "Payments scenario 4954", "data": {"sku": "SKU4954", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4954@example.com", "threshold": 540}},
    {"id": "PAYMENTS-4955", "title": "Payments scenario 4955", "data": {"sku": "SKU4955", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4955@example.com", "threshold": 550}},
    {"id": "PAYMENTS-4956", "title": "Payments scenario 4956", "data": {"sku": "SKU4956", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4956@example.com", "threshold": 560}},
    {"id": "PAYMENTS-4957", "title": "Payments scenario 4957", "data": {"sku": "SKU4957", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4957@example.com", "threshold": 570}},
    {"id": "PAYMENTS-4958", "title": "Payments scenario 4958", "data": {"sku": "SKU4958", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4958@example.com", "threshold": 580}},
    {"id": "PAYMENTS-4959", "title": "Payments scenario 4959", "data": {"sku": "SKU4959", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4959@example.com", "threshold": 590}},
    {"id": "PAYMENTS-4960", "title": "Payments scenario 4960", "data": {"sku": "SKU4960", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4960@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
