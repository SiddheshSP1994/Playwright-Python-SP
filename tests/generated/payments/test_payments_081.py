import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4831", "title": "Payments scenario 4831", "data": {"sku": "SKU4831", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4831@example.com", "threshold": 310}},
    {"id": "PAYMENTS-4832", "title": "Payments scenario 4832", "data": {"sku": "SKU4832", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4832@example.com", "threshold": 320}},
    {"id": "PAYMENTS-4833", "title": "Payments scenario 4833", "data": {"sku": "SKU4833", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4833@example.com", "threshold": 330}},
    {"id": "PAYMENTS-4834", "title": "Payments scenario 4834", "data": {"sku": "SKU4834", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4834@example.com", "threshold": 340}},
    {"id": "PAYMENTS-4835", "title": "Payments scenario 4835", "data": {"sku": "SKU4835", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4835@example.com", "threshold": 350}},
    {"id": "PAYMENTS-4836", "title": "Payments scenario 4836", "data": {"sku": "SKU4836", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4836@example.com", "threshold": 360}},
    {"id": "PAYMENTS-4837", "title": "Payments scenario 4837", "data": {"sku": "SKU4837", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4837@example.com", "threshold": 370}},
    {"id": "PAYMENTS-4838", "title": "Payments scenario 4838", "data": {"sku": "SKU4838", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4838@example.com", "threshold": 380}},
    {"id": "PAYMENTS-4839", "title": "Payments scenario 4839", "data": {"sku": "SKU4839", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4839@example.com", "threshold": 390}},
    {"id": "PAYMENTS-4840", "title": "Payments scenario 4840", "data": {"sku": "SKU4840", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4840@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
