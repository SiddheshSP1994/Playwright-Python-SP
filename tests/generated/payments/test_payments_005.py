import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0271", "title": "Payments scenario 271", "data": {"sku": "SKU271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user271@example.com", "threshold": 710}},
    {"id": "PAYMENTS-0272", "title": "Payments scenario 272", "data": {"sku": "SKU272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user272@example.com", "threshold": 720}},
    {"id": "PAYMENTS-0273", "title": "Payments scenario 273", "data": {"sku": "SKU273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user273@example.com", "threshold": 730}},
    {"id": "PAYMENTS-0274", "title": "Payments scenario 274", "data": {"sku": "SKU274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user274@example.com", "threshold": 740}},
    {"id": "PAYMENTS-0275", "title": "Payments scenario 275", "data": {"sku": "SKU275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user275@example.com", "threshold": 750}},
    {"id": "PAYMENTS-0276", "title": "Payments scenario 276", "data": {"sku": "SKU276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user276@example.com", "threshold": 760}},
    {"id": "PAYMENTS-0277", "title": "Payments scenario 277", "data": {"sku": "SKU277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user277@example.com", "threshold": 770}},
    {"id": "PAYMENTS-0278", "title": "Payments scenario 278", "data": {"sku": "SKU278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user278@example.com", "threshold": 780}},
    {"id": "PAYMENTS-0279", "title": "Payments scenario 279", "data": {"sku": "SKU279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user279@example.com", "threshold": 790}},
    {"id": "PAYMENTS-0280", "title": "Payments scenario 280", "data": {"sku": "SKU280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user280@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
