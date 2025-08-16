import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8071", "title": "Payments scenario 8071", "data": {"sku": "SKU8071", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8071@example.com", "threshold": 710}},
    {"id": "PAYMENTS-8072", "title": "Payments scenario 8072", "data": {"sku": "SKU8072", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8072@example.com", "threshold": 720}},
    {"id": "PAYMENTS-8073", "title": "Payments scenario 8073", "data": {"sku": "SKU8073", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8073@example.com", "threshold": 730}},
    {"id": "PAYMENTS-8074", "title": "Payments scenario 8074", "data": {"sku": "SKU8074", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8074@example.com", "threshold": 740}},
    {"id": "PAYMENTS-8075", "title": "Payments scenario 8075", "data": {"sku": "SKU8075", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8075@example.com", "threshold": 750}},
    {"id": "PAYMENTS-8076", "title": "Payments scenario 8076", "data": {"sku": "SKU8076", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8076@example.com", "threshold": 760}},
    {"id": "PAYMENTS-8077", "title": "Payments scenario 8077", "data": {"sku": "SKU8077", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8077@example.com", "threshold": 770}},
    {"id": "PAYMENTS-8078", "title": "Payments scenario 8078", "data": {"sku": "SKU8078", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8078@example.com", "threshold": 780}},
    {"id": "PAYMENTS-8079", "title": "Payments scenario 8079", "data": {"sku": "SKU8079", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8079@example.com", "threshold": 790}},
    {"id": "PAYMENTS-8080", "title": "Payments scenario 8080", "data": {"sku": "SKU8080", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8080@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
