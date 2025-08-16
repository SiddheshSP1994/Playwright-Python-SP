import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6881", "title": "Email scenario 6881", "data": {"sku": "SKU6881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6881@example.com", "threshold": 810}},
    {"id": "EMAIL-6882", "title": "Email scenario 6882", "data": {"sku": "SKU6882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6882@example.com", "threshold": 820}},
    {"id": "EMAIL-6883", "title": "Email scenario 6883", "data": {"sku": "SKU6883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6883@example.com", "threshold": 830}},
    {"id": "EMAIL-6884", "title": "Email scenario 6884", "data": {"sku": "SKU6884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6884@example.com", "threshold": 840}},
    {"id": "EMAIL-6885", "title": "Email scenario 6885", "data": {"sku": "SKU6885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6885@example.com", "threshold": 850}},
    {"id": "EMAIL-6886", "title": "Email scenario 6886", "data": {"sku": "SKU6886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6886@example.com", "threshold": 860}},
    {"id": "EMAIL-6887", "title": "Email scenario 6887", "data": {"sku": "SKU6887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6887@example.com", "threshold": 870}},
    {"id": "EMAIL-6888", "title": "Email scenario 6888", "data": {"sku": "SKU6888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6888@example.com", "threshold": 880}},
    {"id": "EMAIL-6889", "title": "Email scenario 6889", "data": {"sku": "SKU6889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6889@example.com", "threshold": 890}},
    {"id": "EMAIL-6890", "title": "Email scenario 6890", "data": {"sku": "SKU6890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6890@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
