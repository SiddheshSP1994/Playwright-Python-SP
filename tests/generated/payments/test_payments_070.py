import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4171", "title": "Payments scenario 4171", "data": {"sku": "SKU4171", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4171@example.com", "threshold": 710}},
    {"id": "PAYMENTS-4172", "title": "Payments scenario 4172", "data": {"sku": "SKU4172", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4172@example.com", "threshold": 720}},
    {"id": "PAYMENTS-4173", "title": "Payments scenario 4173", "data": {"sku": "SKU4173", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4173@example.com", "threshold": 730}},
    {"id": "PAYMENTS-4174", "title": "Payments scenario 4174", "data": {"sku": "SKU4174", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4174@example.com", "threshold": 740}},
    {"id": "PAYMENTS-4175", "title": "Payments scenario 4175", "data": {"sku": "SKU4175", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4175@example.com", "threshold": 750}},
    {"id": "PAYMENTS-4176", "title": "Payments scenario 4176", "data": {"sku": "SKU4176", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4176@example.com", "threshold": 760}},
    {"id": "PAYMENTS-4177", "title": "Payments scenario 4177", "data": {"sku": "SKU4177", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4177@example.com", "threshold": 770}},
    {"id": "PAYMENTS-4178", "title": "Payments scenario 4178", "data": {"sku": "SKU4178", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4178@example.com", "threshold": 780}},
    {"id": "PAYMENTS-4179", "title": "Payments scenario 4179", "data": {"sku": "SKU4179", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4179@example.com", "threshold": 790}},
    {"id": "PAYMENTS-4180", "title": "Payments scenario 4180", "data": {"sku": "SKU4180", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4180@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
