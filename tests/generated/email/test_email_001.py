import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0041", "title": "Email scenario 41", "data": {"sku": "SKU41", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user41@example.com", "threshold": 410}},
    {"id": "EMAIL-0042", "title": "Email scenario 42", "data": {"sku": "SKU42", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user42@example.com", "threshold": 420}},
    {"id": "EMAIL-0043", "title": "Email scenario 43", "data": {"sku": "SKU43", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user43@example.com", "threshold": 430}},
    {"id": "EMAIL-0044", "title": "Email scenario 44", "data": {"sku": "SKU44", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user44@example.com", "threshold": 440}},
    {"id": "EMAIL-0045", "title": "Email scenario 45", "data": {"sku": "SKU45", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user45@example.com", "threshold": 450}},
    {"id": "EMAIL-0046", "title": "Email scenario 46", "data": {"sku": "SKU46", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user46@example.com", "threshold": 460}},
    {"id": "EMAIL-0047", "title": "Email scenario 47", "data": {"sku": "SKU47", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user47@example.com", "threshold": 470}},
    {"id": "EMAIL-0048", "title": "Email scenario 48", "data": {"sku": "SKU48", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user48@example.com", "threshold": 480}},
    {"id": "EMAIL-0049", "title": "Email scenario 49", "data": {"sku": "SKU49", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user49@example.com", "threshold": 490}},
    {"id": "EMAIL-0050", "title": "Email scenario 50", "data": {"sku": "SKU50", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user50@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
