import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8671", "title": "Payments scenario 8671", "data": {"sku": "SKU8671", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8671@example.com", "threshold": 710}},
    {"id": "PAYMENTS-8672", "title": "Payments scenario 8672", "data": {"sku": "SKU8672", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8672@example.com", "threshold": 720}},
    {"id": "PAYMENTS-8673", "title": "Payments scenario 8673", "data": {"sku": "SKU8673", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8673@example.com", "threshold": 730}},
    {"id": "PAYMENTS-8674", "title": "Payments scenario 8674", "data": {"sku": "SKU8674", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8674@example.com", "threshold": 740}},
    {"id": "PAYMENTS-8675", "title": "Payments scenario 8675", "data": {"sku": "SKU8675", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8675@example.com", "threshold": 750}},
    {"id": "PAYMENTS-8676", "title": "Payments scenario 8676", "data": {"sku": "SKU8676", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8676@example.com", "threshold": 760}},
    {"id": "PAYMENTS-8677", "title": "Payments scenario 8677", "data": {"sku": "SKU8677", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8677@example.com", "threshold": 770}},
    {"id": "PAYMENTS-8678", "title": "Payments scenario 8678", "data": {"sku": "SKU8678", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8678@example.com", "threshold": 780}},
    {"id": "PAYMENTS-8679", "title": "Payments scenario 8679", "data": {"sku": "SKU8679", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8679@example.com", "threshold": 790}},
    {"id": "PAYMENTS-8680", "title": "Payments scenario 8680", "data": {"sku": "SKU8680", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8680@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
