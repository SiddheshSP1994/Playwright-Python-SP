import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2141", "title": "Email scenario 2141", "data": {"sku": "SKU2141", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2141@example.com", "threshold": 410}},
    {"id": "EMAIL-2142", "title": "Email scenario 2142", "data": {"sku": "SKU2142", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2142@example.com", "threshold": 420}},
    {"id": "EMAIL-2143", "title": "Email scenario 2143", "data": {"sku": "SKU2143", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2143@example.com", "threshold": 430}},
    {"id": "EMAIL-2144", "title": "Email scenario 2144", "data": {"sku": "SKU2144", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2144@example.com", "threshold": 440}},
    {"id": "EMAIL-2145", "title": "Email scenario 2145", "data": {"sku": "SKU2145", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2145@example.com", "threshold": 450}},
    {"id": "EMAIL-2146", "title": "Email scenario 2146", "data": {"sku": "SKU2146", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2146@example.com", "threshold": 460}},
    {"id": "EMAIL-2147", "title": "Email scenario 2147", "data": {"sku": "SKU2147", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2147@example.com", "threshold": 470}},
    {"id": "EMAIL-2148", "title": "Email scenario 2148", "data": {"sku": "SKU2148", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2148@example.com", "threshold": 480}},
    {"id": "EMAIL-2149", "title": "Email scenario 2149", "data": {"sku": "SKU2149", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2149@example.com", "threshold": 490}},
    {"id": "EMAIL-2150", "title": "Email scenario 2150", "data": {"sku": "SKU2150", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2150@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
