import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2551", "title": "Payments scenario 2551", "data": {"sku": "SKU2551", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2551@example.com", "threshold": 510}},
    {"id": "PAYMENTS-2552", "title": "Payments scenario 2552", "data": {"sku": "SKU2552", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2552@example.com", "threshold": 520}},
    {"id": "PAYMENTS-2553", "title": "Payments scenario 2553", "data": {"sku": "SKU2553", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2553@example.com", "threshold": 530}},
    {"id": "PAYMENTS-2554", "title": "Payments scenario 2554", "data": {"sku": "SKU2554", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2554@example.com", "threshold": 540}},
    {"id": "PAYMENTS-2555", "title": "Payments scenario 2555", "data": {"sku": "SKU2555", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2555@example.com", "threshold": 550}},
    {"id": "PAYMENTS-2556", "title": "Payments scenario 2556", "data": {"sku": "SKU2556", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2556@example.com", "threshold": 560}},
    {"id": "PAYMENTS-2557", "title": "Payments scenario 2557", "data": {"sku": "SKU2557", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2557@example.com", "threshold": 570}},
    {"id": "PAYMENTS-2558", "title": "Payments scenario 2558", "data": {"sku": "SKU2558", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2558@example.com", "threshold": 580}},
    {"id": "PAYMENTS-2559", "title": "Payments scenario 2559", "data": {"sku": "SKU2559", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2559@example.com", "threshold": 590}},
    {"id": "PAYMENTS-2560", "title": "Payments scenario 2560", "data": {"sku": "SKU2560", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2560@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
