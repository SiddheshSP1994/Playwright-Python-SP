import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4541", "title": "Email scenario 4541", "data": {"sku": "SKU4541", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4541@example.com", "threshold": 410}},
    {"id": "EMAIL-4542", "title": "Email scenario 4542", "data": {"sku": "SKU4542", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4542@example.com", "threshold": 420}},
    {"id": "EMAIL-4543", "title": "Email scenario 4543", "data": {"sku": "SKU4543", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4543@example.com", "threshold": 430}},
    {"id": "EMAIL-4544", "title": "Email scenario 4544", "data": {"sku": "SKU4544", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4544@example.com", "threshold": 440}},
    {"id": "EMAIL-4545", "title": "Email scenario 4545", "data": {"sku": "SKU4545", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4545@example.com", "threshold": 450}},
    {"id": "EMAIL-4546", "title": "Email scenario 4546", "data": {"sku": "SKU4546", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4546@example.com", "threshold": 460}},
    {"id": "EMAIL-4547", "title": "Email scenario 4547", "data": {"sku": "SKU4547", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4547@example.com", "threshold": 470}},
    {"id": "EMAIL-4548", "title": "Email scenario 4548", "data": {"sku": "SKU4548", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4548@example.com", "threshold": 480}},
    {"id": "EMAIL-4549", "title": "Email scenario 4549", "data": {"sku": "SKU4549", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4549@example.com", "threshold": 490}},
    {"id": "EMAIL-4550", "title": "Email scenario 4550", "data": {"sku": "SKU4550", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4550@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
