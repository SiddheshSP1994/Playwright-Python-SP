import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2311", "title": "Payments scenario 2311", "data": {"sku": "SKU2311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2311@example.com", "threshold": 110}},
    {"id": "PAYMENTS-2312", "title": "Payments scenario 2312", "data": {"sku": "SKU2312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2312@example.com", "threshold": 120}},
    {"id": "PAYMENTS-2313", "title": "Payments scenario 2313", "data": {"sku": "SKU2313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2313@example.com", "threshold": 130}},
    {"id": "PAYMENTS-2314", "title": "Payments scenario 2314", "data": {"sku": "SKU2314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2314@example.com", "threshold": 140}},
    {"id": "PAYMENTS-2315", "title": "Payments scenario 2315", "data": {"sku": "SKU2315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2315@example.com", "threshold": 150}},
    {"id": "PAYMENTS-2316", "title": "Payments scenario 2316", "data": {"sku": "SKU2316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2316@example.com", "threshold": 160}},
    {"id": "PAYMENTS-2317", "title": "Payments scenario 2317", "data": {"sku": "SKU2317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2317@example.com", "threshold": 170}},
    {"id": "PAYMENTS-2318", "title": "Payments scenario 2318", "data": {"sku": "SKU2318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2318@example.com", "threshold": 180}},
    {"id": "PAYMENTS-2319", "title": "Payments scenario 2319", "data": {"sku": "SKU2319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2319@example.com", "threshold": 190}},
    {"id": "PAYMENTS-2320", "title": "Payments scenario 2320", "data": {"sku": "SKU2320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2320@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
