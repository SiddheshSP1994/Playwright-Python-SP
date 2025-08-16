import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6821", "title": "Email scenario 6821", "data": {"sku": "SKU6821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6821@example.com", "threshold": 210}},
    {"id": "EMAIL-6822", "title": "Email scenario 6822", "data": {"sku": "SKU6822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6822@example.com", "threshold": 220}},
    {"id": "EMAIL-6823", "title": "Email scenario 6823", "data": {"sku": "SKU6823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6823@example.com", "threshold": 230}},
    {"id": "EMAIL-6824", "title": "Email scenario 6824", "data": {"sku": "SKU6824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6824@example.com", "threshold": 240}},
    {"id": "EMAIL-6825", "title": "Email scenario 6825", "data": {"sku": "SKU6825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6825@example.com", "threshold": 250}},
    {"id": "EMAIL-6826", "title": "Email scenario 6826", "data": {"sku": "SKU6826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6826@example.com", "threshold": 260}},
    {"id": "EMAIL-6827", "title": "Email scenario 6827", "data": {"sku": "SKU6827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6827@example.com", "threshold": 270}},
    {"id": "EMAIL-6828", "title": "Email scenario 6828", "data": {"sku": "SKU6828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6828@example.com", "threshold": 280}},
    {"id": "EMAIL-6829", "title": "Email scenario 6829", "data": {"sku": "SKU6829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6829@example.com", "threshold": 290}},
    {"id": "EMAIL-6830", "title": "Email scenario 6830", "data": {"sku": "SKU6830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6830@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
