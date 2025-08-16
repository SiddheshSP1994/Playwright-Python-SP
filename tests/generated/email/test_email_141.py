import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8441", "title": "Email scenario 8441", "data": {"sku": "SKU8441", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8441@example.com", "threshold": 410}},
    {"id": "EMAIL-8442", "title": "Email scenario 8442", "data": {"sku": "SKU8442", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8442@example.com", "threshold": 420}},
    {"id": "EMAIL-8443", "title": "Email scenario 8443", "data": {"sku": "SKU8443", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8443@example.com", "threshold": 430}},
    {"id": "EMAIL-8444", "title": "Email scenario 8444", "data": {"sku": "SKU8444", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8444@example.com", "threshold": 440}},
    {"id": "EMAIL-8445", "title": "Email scenario 8445", "data": {"sku": "SKU8445", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8445@example.com", "threshold": 450}},
    {"id": "EMAIL-8446", "title": "Email scenario 8446", "data": {"sku": "SKU8446", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8446@example.com", "threshold": 460}},
    {"id": "EMAIL-8447", "title": "Email scenario 8447", "data": {"sku": "SKU8447", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8447@example.com", "threshold": 470}},
    {"id": "EMAIL-8448", "title": "Email scenario 8448", "data": {"sku": "SKU8448", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8448@example.com", "threshold": 480}},
    {"id": "EMAIL-8449", "title": "Email scenario 8449", "data": {"sku": "SKU8449", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8449@example.com", "threshold": 490}},
    {"id": "EMAIL-8450", "title": "Email scenario 8450", "data": {"sku": "SKU8450", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8450@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
