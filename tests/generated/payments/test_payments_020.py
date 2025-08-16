import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1171", "title": "Payments scenario 1171", "data": {"sku": "SKU1171", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1171@example.com", "threshold": 710}},
    {"id": "PAYMENTS-1172", "title": "Payments scenario 1172", "data": {"sku": "SKU1172", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1172@example.com", "threshold": 720}},
    {"id": "PAYMENTS-1173", "title": "Payments scenario 1173", "data": {"sku": "SKU1173", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1173@example.com", "threshold": 730}},
    {"id": "PAYMENTS-1174", "title": "Payments scenario 1174", "data": {"sku": "SKU1174", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1174@example.com", "threshold": 740}},
    {"id": "PAYMENTS-1175", "title": "Payments scenario 1175", "data": {"sku": "SKU1175", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1175@example.com", "threshold": 750}},
    {"id": "PAYMENTS-1176", "title": "Payments scenario 1176", "data": {"sku": "SKU1176", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1176@example.com", "threshold": 760}},
    {"id": "PAYMENTS-1177", "title": "Payments scenario 1177", "data": {"sku": "SKU1177", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1177@example.com", "threshold": 770}},
    {"id": "PAYMENTS-1178", "title": "Payments scenario 1178", "data": {"sku": "SKU1178", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1178@example.com", "threshold": 780}},
    {"id": "PAYMENTS-1179", "title": "Payments scenario 1179", "data": {"sku": "SKU1179", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1179@example.com", "threshold": 790}},
    {"id": "PAYMENTS-1180", "title": "Payments scenario 1180", "data": {"sku": "SKU1180", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1180@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
