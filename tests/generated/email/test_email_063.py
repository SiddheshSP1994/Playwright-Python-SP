import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3761", "title": "Email scenario 3761", "data": {"sku": "SKU3761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3761@example.com", "threshold": 610}},
    {"id": "EMAIL-3762", "title": "Email scenario 3762", "data": {"sku": "SKU3762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3762@example.com", "threshold": 620}},
    {"id": "EMAIL-3763", "title": "Email scenario 3763", "data": {"sku": "SKU3763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3763@example.com", "threshold": 630}},
    {"id": "EMAIL-3764", "title": "Email scenario 3764", "data": {"sku": "SKU3764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3764@example.com", "threshold": 640}},
    {"id": "EMAIL-3765", "title": "Email scenario 3765", "data": {"sku": "SKU3765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3765@example.com", "threshold": 650}},
    {"id": "EMAIL-3766", "title": "Email scenario 3766", "data": {"sku": "SKU3766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3766@example.com", "threshold": 660}},
    {"id": "EMAIL-3767", "title": "Email scenario 3767", "data": {"sku": "SKU3767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3767@example.com", "threshold": 670}},
    {"id": "EMAIL-3768", "title": "Email scenario 3768", "data": {"sku": "SKU3768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3768@example.com", "threshold": 680}},
    {"id": "EMAIL-3769", "title": "Email scenario 3769", "data": {"sku": "SKU3769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3769@example.com", "threshold": 690}},
    {"id": "EMAIL-3770", "title": "Email scenario 3770", "data": {"sku": "SKU3770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3770@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
