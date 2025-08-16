import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7171", "title": "Payments scenario 7171", "data": {"sku": "SKU7171", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7171@example.com", "threshold": 710}},
    {"id": "PAYMENTS-7172", "title": "Payments scenario 7172", "data": {"sku": "SKU7172", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7172@example.com", "threshold": 720}},
    {"id": "PAYMENTS-7173", "title": "Payments scenario 7173", "data": {"sku": "SKU7173", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7173@example.com", "threshold": 730}},
    {"id": "PAYMENTS-7174", "title": "Payments scenario 7174", "data": {"sku": "SKU7174", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7174@example.com", "threshold": 740}},
    {"id": "PAYMENTS-7175", "title": "Payments scenario 7175", "data": {"sku": "SKU7175", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7175@example.com", "threshold": 750}},
    {"id": "PAYMENTS-7176", "title": "Payments scenario 7176", "data": {"sku": "SKU7176", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7176@example.com", "threshold": 760}},
    {"id": "PAYMENTS-7177", "title": "Payments scenario 7177", "data": {"sku": "SKU7177", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7177@example.com", "threshold": 770}},
    {"id": "PAYMENTS-7178", "title": "Payments scenario 7178", "data": {"sku": "SKU7178", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7178@example.com", "threshold": 780}},
    {"id": "PAYMENTS-7179", "title": "Payments scenario 7179", "data": {"sku": "SKU7179", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7179@example.com", "threshold": 790}},
    {"id": "PAYMENTS-7180", "title": "Payments scenario 7180", "data": {"sku": "SKU7180", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7180@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
