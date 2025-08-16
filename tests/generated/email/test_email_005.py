import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0281", "title": "Email scenario 281", "data": {"sku": "SKU281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user281@example.com", "threshold": 810}},
    {"id": "EMAIL-0282", "title": "Email scenario 282", "data": {"sku": "SKU282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user282@example.com", "threshold": 820}},
    {"id": "EMAIL-0283", "title": "Email scenario 283", "data": {"sku": "SKU283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user283@example.com", "threshold": 830}},
    {"id": "EMAIL-0284", "title": "Email scenario 284", "data": {"sku": "SKU284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user284@example.com", "threshold": 840}},
    {"id": "EMAIL-0285", "title": "Email scenario 285", "data": {"sku": "SKU285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user285@example.com", "threshold": 850}},
    {"id": "EMAIL-0286", "title": "Email scenario 286", "data": {"sku": "SKU286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user286@example.com", "threshold": 860}},
    {"id": "EMAIL-0287", "title": "Email scenario 287", "data": {"sku": "SKU287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user287@example.com", "threshold": 870}},
    {"id": "EMAIL-0288", "title": "Email scenario 288", "data": {"sku": "SKU288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user288@example.com", "threshold": 880}},
    {"id": "EMAIL-0289", "title": "Email scenario 289", "data": {"sku": "SKU289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user289@example.com", "threshold": 890}},
    {"id": "EMAIL-0290", "title": "Email scenario 290", "data": {"sku": "SKU290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user290@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
