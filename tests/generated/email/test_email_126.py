import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7541", "title": "Email scenario 7541", "data": {"sku": "SKU7541", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7541@example.com", "threshold": 410}},
    {"id": "EMAIL-7542", "title": "Email scenario 7542", "data": {"sku": "SKU7542", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7542@example.com", "threshold": 420}},
    {"id": "EMAIL-7543", "title": "Email scenario 7543", "data": {"sku": "SKU7543", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7543@example.com", "threshold": 430}},
    {"id": "EMAIL-7544", "title": "Email scenario 7544", "data": {"sku": "SKU7544", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7544@example.com", "threshold": 440}},
    {"id": "EMAIL-7545", "title": "Email scenario 7545", "data": {"sku": "SKU7545", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7545@example.com", "threshold": 450}},
    {"id": "EMAIL-7546", "title": "Email scenario 7546", "data": {"sku": "SKU7546", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7546@example.com", "threshold": 460}},
    {"id": "EMAIL-7547", "title": "Email scenario 7547", "data": {"sku": "SKU7547", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7547@example.com", "threshold": 470}},
    {"id": "EMAIL-7548", "title": "Email scenario 7548", "data": {"sku": "SKU7548", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7548@example.com", "threshold": 480}},
    {"id": "EMAIL-7549", "title": "Email scenario 7549", "data": {"sku": "SKU7549", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7549@example.com", "threshold": 490}},
    {"id": "EMAIL-7550", "title": "Email scenario 7550", "data": {"sku": "SKU7550", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7550@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
