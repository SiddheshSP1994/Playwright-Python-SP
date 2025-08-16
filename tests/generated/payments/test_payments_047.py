import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2791", "title": "Payments scenario 2791", "data": {"sku": "SKU2791", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2791@example.com", "threshold": 910}},
    {"id": "PAYMENTS-2792", "title": "Payments scenario 2792", "data": {"sku": "SKU2792", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2792@example.com", "threshold": 920}},
    {"id": "PAYMENTS-2793", "title": "Payments scenario 2793", "data": {"sku": "SKU2793", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2793@example.com", "threshold": 930}},
    {"id": "PAYMENTS-2794", "title": "Payments scenario 2794", "data": {"sku": "SKU2794", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2794@example.com", "threshold": 940}},
    {"id": "PAYMENTS-2795", "title": "Payments scenario 2795", "data": {"sku": "SKU2795", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2795@example.com", "threshold": 950}},
    {"id": "PAYMENTS-2796", "title": "Payments scenario 2796", "data": {"sku": "SKU2796", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2796@example.com", "threshold": 960}},
    {"id": "PAYMENTS-2797", "title": "Payments scenario 2797", "data": {"sku": "SKU2797", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2797@example.com", "threshold": 970}},
    {"id": "PAYMENTS-2798", "title": "Payments scenario 2798", "data": {"sku": "SKU2798", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2798@example.com", "threshold": 980}},
    {"id": "PAYMENTS-2799", "title": "Payments scenario 2799", "data": {"sku": "SKU2799", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2799@example.com", "threshold": 990}},
    {"id": "PAYMENTS-2800", "title": "Payments scenario 2800", "data": {"sku": "SKU2800", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2800@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
