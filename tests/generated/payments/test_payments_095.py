import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5671", "title": "Payments scenario 5671", "data": {"sku": "SKU5671", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5671@example.com", "threshold": 710}},
    {"id": "PAYMENTS-5672", "title": "Payments scenario 5672", "data": {"sku": "SKU5672", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5672@example.com", "threshold": 720}},
    {"id": "PAYMENTS-5673", "title": "Payments scenario 5673", "data": {"sku": "SKU5673", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5673@example.com", "threshold": 730}},
    {"id": "PAYMENTS-5674", "title": "Payments scenario 5674", "data": {"sku": "SKU5674", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5674@example.com", "threshold": 740}},
    {"id": "PAYMENTS-5675", "title": "Payments scenario 5675", "data": {"sku": "SKU5675", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5675@example.com", "threshold": 750}},
    {"id": "PAYMENTS-5676", "title": "Payments scenario 5676", "data": {"sku": "SKU5676", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5676@example.com", "threshold": 760}},
    {"id": "PAYMENTS-5677", "title": "Payments scenario 5677", "data": {"sku": "SKU5677", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5677@example.com", "threshold": 770}},
    {"id": "PAYMENTS-5678", "title": "Payments scenario 5678", "data": {"sku": "SKU5678", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5678@example.com", "threshold": 780}},
    {"id": "PAYMENTS-5679", "title": "Payments scenario 5679", "data": {"sku": "SKU5679", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5679@example.com", "threshold": 790}},
    {"id": "PAYMENTS-5680", "title": "Payments scenario 5680", "data": {"sku": "SKU5680", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5680@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
