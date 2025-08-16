import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2131", "title": "Payments scenario 2131", "data": {"sku": "SKU2131", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2131@example.com", "threshold": 310}},
    {"id": "PAYMENTS-2132", "title": "Payments scenario 2132", "data": {"sku": "SKU2132", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2132@example.com", "threshold": 320}},
    {"id": "PAYMENTS-2133", "title": "Payments scenario 2133", "data": {"sku": "SKU2133", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2133@example.com", "threshold": 330}},
    {"id": "PAYMENTS-2134", "title": "Payments scenario 2134", "data": {"sku": "SKU2134", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2134@example.com", "threshold": 340}},
    {"id": "PAYMENTS-2135", "title": "Payments scenario 2135", "data": {"sku": "SKU2135", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2135@example.com", "threshold": 350}},
    {"id": "PAYMENTS-2136", "title": "Payments scenario 2136", "data": {"sku": "SKU2136", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2136@example.com", "threshold": 360}},
    {"id": "PAYMENTS-2137", "title": "Payments scenario 2137", "data": {"sku": "SKU2137", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2137@example.com", "threshold": 370}},
    {"id": "PAYMENTS-2138", "title": "Payments scenario 2138", "data": {"sku": "SKU2138", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2138@example.com", "threshold": 380}},
    {"id": "PAYMENTS-2139", "title": "Payments scenario 2139", "data": {"sku": "SKU2139", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2139@example.com", "threshold": 390}},
    {"id": "PAYMENTS-2140", "title": "Payments scenario 2140", "data": {"sku": "SKU2140", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2140@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
