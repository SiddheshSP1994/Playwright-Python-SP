import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1831", "title": "Payments scenario 1831", "data": {"sku": "SKU1831", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1831@example.com", "threshold": 310}},
    {"id": "PAYMENTS-1832", "title": "Payments scenario 1832", "data": {"sku": "SKU1832", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1832@example.com", "threshold": 320}},
    {"id": "PAYMENTS-1833", "title": "Payments scenario 1833", "data": {"sku": "SKU1833", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1833@example.com", "threshold": 330}},
    {"id": "PAYMENTS-1834", "title": "Payments scenario 1834", "data": {"sku": "SKU1834", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1834@example.com", "threshold": 340}},
    {"id": "PAYMENTS-1835", "title": "Payments scenario 1835", "data": {"sku": "SKU1835", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1835@example.com", "threshold": 350}},
    {"id": "PAYMENTS-1836", "title": "Payments scenario 1836", "data": {"sku": "SKU1836", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1836@example.com", "threshold": 360}},
    {"id": "PAYMENTS-1837", "title": "Payments scenario 1837", "data": {"sku": "SKU1837", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1837@example.com", "threshold": 370}},
    {"id": "PAYMENTS-1838", "title": "Payments scenario 1838", "data": {"sku": "SKU1838", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1838@example.com", "threshold": 380}},
    {"id": "PAYMENTS-1839", "title": "Payments scenario 1839", "data": {"sku": "SKU1839", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1839@example.com", "threshold": 390}},
    {"id": "PAYMENTS-1840", "title": "Payments scenario 1840", "data": {"sku": "SKU1840", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1840@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
