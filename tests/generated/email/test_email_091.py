import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5441", "title": "Email scenario 5441", "data": {"sku": "SKU5441", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5441@example.com", "threshold": 410}},
    {"id": "EMAIL-5442", "title": "Email scenario 5442", "data": {"sku": "SKU5442", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5442@example.com", "threshold": 420}},
    {"id": "EMAIL-5443", "title": "Email scenario 5443", "data": {"sku": "SKU5443", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5443@example.com", "threshold": 430}},
    {"id": "EMAIL-5444", "title": "Email scenario 5444", "data": {"sku": "SKU5444", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5444@example.com", "threshold": 440}},
    {"id": "EMAIL-5445", "title": "Email scenario 5445", "data": {"sku": "SKU5445", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5445@example.com", "threshold": 450}},
    {"id": "EMAIL-5446", "title": "Email scenario 5446", "data": {"sku": "SKU5446", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5446@example.com", "threshold": 460}},
    {"id": "EMAIL-5447", "title": "Email scenario 5447", "data": {"sku": "SKU5447", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5447@example.com", "threshold": 470}},
    {"id": "EMAIL-5448", "title": "Email scenario 5448", "data": {"sku": "SKU5448", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5448@example.com", "threshold": 480}},
    {"id": "EMAIL-5449", "title": "Email scenario 5449", "data": {"sku": "SKU5449", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5449@example.com", "threshold": 490}},
    {"id": "EMAIL-5450", "title": "Email scenario 5450", "data": {"sku": "SKU5450", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5450@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
