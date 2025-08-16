import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1531", "title": "Payments scenario 1531", "data": {"sku": "SKU1531", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1531@example.com", "threshold": 310}},
    {"id": "PAYMENTS-1532", "title": "Payments scenario 1532", "data": {"sku": "SKU1532", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1532@example.com", "threshold": 320}},
    {"id": "PAYMENTS-1533", "title": "Payments scenario 1533", "data": {"sku": "SKU1533", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1533@example.com", "threshold": 330}},
    {"id": "PAYMENTS-1534", "title": "Payments scenario 1534", "data": {"sku": "SKU1534", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1534@example.com", "threshold": 340}},
    {"id": "PAYMENTS-1535", "title": "Payments scenario 1535", "data": {"sku": "SKU1535", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1535@example.com", "threshold": 350}},
    {"id": "PAYMENTS-1536", "title": "Payments scenario 1536", "data": {"sku": "SKU1536", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1536@example.com", "threshold": 360}},
    {"id": "PAYMENTS-1537", "title": "Payments scenario 1537", "data": {"sku": "SKU1537", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1537@example.com", "threshold": 370}},
    {"id": "PAYMENTS-1538", "title": "Payments scenario 1538", "data": {"sku": "SKU1538", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1538@example.com", "threshold": 380}},
    {"id": "PAYMENTS-1539", "title": "Payments scenario 1539", "data": {"sku": "SKU1539", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1539@example.com", "threshold": 390}},
    {"id": "PAYMENTS-1540", "title": "Payments scenario 1540", "data": {"sku": "SKU1540", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1540@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
