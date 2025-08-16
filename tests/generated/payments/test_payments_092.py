import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5491", "title": "Payments scenario 5491", "data": {"sku": "SKU5491", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5491@example.com", "threshold": 910}},
    {"id": "PAYMENTS-5492", "title": "Payments scenario 5492", "data": {"sku": "SKU5492", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5492@example.com", "threshold": 920}},
    {"id": "PAYMENTS-5493", "title": "Payments scenario 5493", "data": {"sku": "SKU5493", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5493@example.com", "threshold": 930}},
    {"id": "PAYMENTS-5494", "title": "Payments scenario 5494", "data": {"sku": "SKU5494", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5494@example.com", "threshold": 940}},
    {"id": "PAYMENTS-5495", "title": "Payments scenario 5495", "data": {"sku": "SKU5495", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5495@example.com", "threshold": 950}},
    {"id": "PAYMENTS-5496", "title": "Payments scenario 5496", "data": {"sku": "SKU5496", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5496@example.com", "threshold": 960}},
    {"id": "PAYMENTS-5497", "title": "Payments scenario 5497", "data": {"sku": "SKU5497", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5497@example.com", "threshold": 970}},
    {"id": "PAYMENTS-5498", "title": "Payments scenario 5498", "data": {"sku": "SKU5498", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5498@example.com", "threshold": 980}},
    {"id": "PAYMENTS-5499", "title": "Payments scenario 5499", "data": {"sku": "SKU5499", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5499@example.com", "threshold": 990}},
    {"id": "PAYMENTS-5500", "title": "Payments scenario 5500", "data": {"sku": "SKU5500", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5500@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
