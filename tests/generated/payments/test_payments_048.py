import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2851", "title": "Payments scenario 2851", "data": {"sku": "SKU2851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2851@example.com", "threshold": 510}},
    {"id": "PAYMENTS-2852", "title": "Payments scenario 2852", "data": {"sku": "SKU2852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2852@example.com", "threshold": 520}},
    {"id": "PAYMENTS-2853", "title": "Payments scenario 2853", "data": {"sku": "SKU2853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2853@example.com", "threshold": 530}},
    {"id": "PAYMENTS-2854", "title": "Payments scenario 2854", "data": {"sku": "SKU2854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2854@example.com", "threshold": 540}},
    {"id": "PAYMENTS-2855", "title": "Payments scenario 2855", "data": {"sku": "SKU2855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2855@example.com", "threshold": 550}},
    {"id": "PAYMENTS-2856", "title": "Payments scenario 2856", "data": {"sku": "SKU2856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2856@example.com", "threshold": 560}},
    {"id": "PAYMENTS-2857", "title": "Payments scenario 2857", "data": {"sku": "SKU2857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2857@example.com", "threshold": 570}},
    {"id": "PAYMENTS-2858", "title": "Payments scenario 2858", "data": {"sku": "SKU2858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2858@example.com", "threshold": 580}},
    {"id": "PAYMENTS-2859", "title": "Payments scenario 2859", "data": {"sku": "SKU2859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2859@example.com", "threshold": 590}},
    {"id": "PAYMENTS-2860", "title": "Payments scenario 2860", "data": {"sku": "SKU2860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2860@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
