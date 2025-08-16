import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5071", "title": "Payments scenario 5071", "data": {"sku": "SKU5071", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5071@example.com", "threshold": 710}},
    {"id": "PAYMENTS-5072", "title": "Payments scenario 5072", "data": {"sku": "SKU5072", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5072@example.com", "threshold": 720}},
    {"id": "PAYMENTS-5073", "title": "Payments scenario 5073", "data": {"sku": "SKU5073", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5073@example.com", "threshold": 730}},
    {"id": "PAYMENTS-5074", "title": "Payments scenario 5074", "data": {"sku": "SKU5074", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5074@example.com", "threshold": 740}},
    {"id": "PAYMENTS-5075", "title": "Payments scenario 5075", "data": {"sku": "SKU5075", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5075@example.com", "threshold": 750}},
    {"id": "PAYMENTS-5076", "title": "Payments scenario 5076", "data": {"sku": "SKU5076", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5076@example.com", "threshold": 760}},
    {"id": "PAYMENTS-5077", "title": "Payments scenario 5077", "data": {"sku": "SKU5077", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5077@example.com", "threshold": 770}},
    {"id": "PAYMENTS-5078", "title": "Payments scenario 5078", "data": {"sku": "SKU5078", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5078@example.com", "threshold": 780}},
    {"id": "PAYMENTS-5079", "title": "Payments scenario 5079", "data": {"sku": "SKU5079", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5079@example.com", "threshold": 790}},
    {"id": "PAYMENTS-5080", "title": "Payments scenario 5080", "data": {"sku": "SKU5080", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5080@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
