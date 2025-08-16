import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8011", "title": "Payments scenario 8011", "data": {"sku": "SKU8011", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8011@example.com", "threshold": 110}},
    {"id": "PAYMENTS-8012", "title": "Payments scenario 8012", "data": {"sku": "SKU8012", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8012@example.com", "threshold": 120}},
    {"id": "PAYMENTS-8013", "title": "Payments scenario 8013", "data": {"sku": "SKU8013", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8013@example.com", "threshold": 130}},
    {"id": "PAYMENTS-8014", "title": "Payments scenario 8014", "data": {"sku": "SKU8014", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8014@example.com", "threshold": 140}},
    {"id": "PAYMENTS-8015", "title": "Payments scenario 8015", "data": {"sku": "SKU8015", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8015@example.com", "threshold": 150}},
    {"id": "PAYMENTS-8016", "title": "Payments scenario 8016", "data": {"sku": "SKU8016", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8016@example.com", "threshold": 160}},
    {"id": "PAYMENTS-8017", "title": "Payments scenario 8017", "data": {"sku": "SKU8017", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8017@example.com", "threshold": 170}},
    {"id": "PAYMENTS-8018", "title": "Payments scenario 8018", "data": {"sku": "SKU8018", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8018@example.com", "threshold": 180}},
    {"id": "PAYMENTS-8019", "title": "Payments scenario 8019", "data": {"sku": "SKU8019", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8019@example.com", "threshold": 190}},
    {"id": "PAYMENTS-8020", "title": "Payments scenario 8020", "data": {"sku": "SKU8020", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8020@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
