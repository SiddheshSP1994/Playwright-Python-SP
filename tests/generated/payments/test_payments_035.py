import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2071", "title": "Payments scenario 2071", "data": {"sku": "SKU2071", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2071@example.com", "threshold": 710}},
    {"id": "PAYMENTS-2072", "title": "Payments scenario 2072", "data": {"sku": "SKU2072", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2072@example.com", "threshold": 720}},
    {"id": "PAYMENTS-2073", "title": "Payments scenario 2073", "data": {"sku": "SKU2073", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2073@example.com", "threshold": 730}},
    {"id": "PAYMENTS-2074", "title": "Payments scenario 2074", "data": {"sku": "SKU2074", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2074@example.com", "threshold": 740}},
    {"id": "PAYMENTS-2075", "title": "Payments scenario 2075", "data": {"sku": "SKU2075", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2075@example.com", "threshold": 750}},
    {"id": "PAYMENTS-2076", "title": "Payments scenario 2076", "data": {"sku": "SKU2076", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2076@example.com", "threshold": 760}},
    {"id": "PAYMENTS-2077", "title": "Payments scenario 2077", "data": {"sku": "SKU2077", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2077@example.com", "threshold": 770}},
    {"id": "PAYMENTS-2078", "title": "Payments scenario 2078", "data": {"sku": "SKU2078", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2078@example.com", "threshold": 780}},
    {"id": "PAYMENTS-2079", "title": "Payments scenario 2079", "data": {"sku": "SKU2079", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2079@example.com", "threshold": 790}},
    {"id": "PAYMENTS-2080", "title": "Payments scenario 2080", "data": {"sku": "SKU2080", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2080@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
