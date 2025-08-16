import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9821", "title": "Email scenario 9821", "data": {"sku": "SKU9821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9821@example.com", "threshold": 210}},
    {"id": "EMAIL-9822", "title": "Email scenario 9822", "data": {"sku": "SKU9822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9822@example.com", "threshold": 220}},
    {"id": "EMAIL-9823", "title": "Email scenario 9823", "data": {"sku": "SKU9823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9823@example.com", "threshold": 230}},
    {"id": "EMAIL-9824", "title": "Email scenario 9824", "data": {"sku": "SKU9824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9824@example.com", "threshold": 240}},
    {"id": "EMAIL-9825", "title": "Email scenario 9825", "data": {"sku": "SKU9825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9825@example.com", "threshold": 250}},
    {"id": "EMAIL-9826", "title": "Email scenario 9826", "data": {"sku": "SKU9826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9826@example.com", "threshold": 260}},
    {"id": "EMAIL-9827", "title": "Email scenario 9827", "data": {"sku": "SKU9827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9827@example.com", "threshold": 270}},
    {"id": "EMAIL-9828", "title": "Email scenario 9828", "data": {"sku": "SKU9828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9828@example.com", "threshold": 280}},
    {"id": "EMAIL-9829", "title": "Email scenario 9829", "data": {"sku": "SKU9829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9829@example.com", "threshold": 290}},
    {"id": "EMAIL-9830", "title": "Email scenario 9830", "data": {"sku": "SKU9830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9830@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
