import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1051", "title": "Payments scenario 1051", "data": {"sku": "SKU1051", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1051@example.com", "threshold": 510}},
    {"id": "PAYMENTS-1052", "title": "Payments scenario 1052", "data": {"sku": "SKU1052", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1052@example.com", "threshold": 520}},
    {"id": "PAYMENTS-1053", "title": "Payments scenario 1053", "data": {"sku": "SKU1053", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1053@example.com", "threshold": 530}},
    {"id": "PAYMENTS-1054", "title": "Payments scenario 1054", "data": {"sku": "SKU1054", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1054@example.com", "threshold": 540}},
    {"id": "PAYMENTS-1055", "title": "Payments scenario 1055", "data": {"sku": "SKU1055", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1055@example.com", "threshold": 550}},
    {"id": "PAYMENTS-1056", "title": "Payments scenario 1056", "data": {"sku": "SKU1056", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1056@example.com", "threshold": 560}},
    {"id": "PAYMENTS-1057", "title": "Payments scenario 1057", "data": {"sku": "SKU1057", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1057@example.com", "threshold": 570}},
    {"id": "PAYMENTS-1058", "title": "Payments scenario 1058", "data": {"sku": "SKU1058", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1058@example.com", "threshold": 580}},
    {"id": "PAYMENTS-1059", "title": "Payments scenario 1059", "data": {"sku": "SKU1059", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1059@example.com", "threshold": 590}},
    {"id": "PAYMENTS-1060", "title": "Payments scenario 1060", "data": {"sku": "SKU1060", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1060@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
