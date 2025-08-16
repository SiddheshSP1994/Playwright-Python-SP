import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8141", "title": "Email scenario 8141", "data": {"sku": "SKU8141", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8141@example.com", "threshold": 410}},
    {"id": "EMAIL-8142", "title": "Email scenario 8142", "data": {"sku": "SKU8142", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8142@example.com", "threshold": 420}},
    {"id": "EMAIL-8143", "title": "Email scenario 8143", "data": {"sku": "SKU8143", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8143@example.com", "threshold": 430}},
    {"id": "EMAIL-8144", "title": "Email scenario 8144", "data": {"sku": "SKU8144", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8144@example.com", "threshold": 440}},
    {"id": "EMAIL-8145", "title": "Email scenario 8145", "data": {"sku": "SKU8145", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8145@example.com", "threshold": 450}},
    {"id": "EMAIL-8146", "title": "Email scenario 8146", "data": {"sku": "SKU8146", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8146@example.com", "threshold": 460}},
    {"id": "EMAIL-8147", "title": "Email scenario 8147", "data": {"sku": "SKU8147", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8147@example.com", "threshold": 470}},
    {"id": "EMAIL-8148", "title": "Email scenario 8148", "data": {"sku": "SKU8148", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8148@example.com", "threshold": 480}},
    {"id": "EMAIL-8149", "title": "Email scenario 8149", "data": {"sku": "SKU8149", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8149@example.com", "threshold": 490}},
    {"id": "EMAIL-8150", "title": "Email scenario 8150", "data": {"sku": "SKU8150", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8150@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
