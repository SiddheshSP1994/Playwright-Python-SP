import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9881", "title": "Email scenario 9881", "data": {"sku": "SKU9881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9881@example.com", "threshold": 810}},
    {"id": "EMAIL-9882", "title": "Email scenario 9882", "data": {"sku": "SKU9882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9882@example.com", "threshold": 820}},
    {"id": "EMAIL-9883", "title": "Email scenario 9883", "data": {"sku": "SKU9883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9883@example.com", "threshold": 830}},
    {"id": "EMAIL-9884", "title": "Email scenario 9884", "data": {"sku": "SKU9884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9884@example.com", "threshold": 840}},
    {"id": "EMAIL-9885", "title": "Email scenario 9885", "data": {"sku": "SKU9885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9885@example.com", "threshold": 850}},
    {"id": "EMAIL-9886", "title": "Email scenario 9886", "data": {"sku": "SKU9886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9886@example.com", "threshold": 860}},
    {"id": "EMAIL-9887", "title": "Email scenario 9887", "data": {"sku": "SKU9887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9887@example.com", "threshold": 870}},
    {"id": "EMAIL-9888", "title": "Email scenario 9888", "data": {"sku": "SKU9888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9888@example.com", "threshold": 880}},
    {"id": "EMAIL-9889", "title": "Email scenario 9889", "data": {"sku": "SKU9889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9889@example.com", "threshold": 890}},
    {"id": "EMAIL-9890", "title": "Email scenario 9890", "data": {"sku": "SKU9890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9890@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
