import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1961", "title": "Email scenario 1961", "data": {"sku": "SKU1961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1961@example.com", "threshold": 610}},
    {"id": "EMAIL-1962", "title": "Email scenario 1962", "data": {"sku": "SKU1962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1962@example.com", "threshold": 620}},
    {"id": "EMAIL-1963", "title": "Email scenario 1963", "data": {"sku": "SKU1963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1963@example.com", "threshold": 630}},
    {"id": "EMAIL-1964", "title": "Email scenario 1964", "data": {"sku": "SKU1964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1964@example.com", "threshold": 640}},
    {"id": "EMAIL-1965", "title": "Email scenario 1965", "data": {"sku": "SKU1965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1965@example.com", "threshold": 650}},
    {"id": "EMAIL-1966", "title": "Email scenario 1966", "data": {"sku": "SKU1966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1966@example.com", "threshold": 660}},
    {"id": "EMAIL-1967", "title": "Email scenario 1967", "data": {"sku": "SKU1967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1967@example.com", "threshold": 670}},
    {"id": "EMAIL-1968", "title": "Email scenario 1968", "data": {"sku": "SKU1968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1968@example.com", "threshold": 680}},
    {"id": "EMAIL-1969", "title": "Email scenario 1969", "data": {"sku": "SKU1969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1969@example.com", "threshold": 690}},
    {"id": "EMAIL-1970", "title": "Email scenario 1970", "data": {"sku": "SKU1970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1970@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
