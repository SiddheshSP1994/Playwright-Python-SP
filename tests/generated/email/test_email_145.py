import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8681", "title": "Email scenario 8681", "data": {"sku": "SKU8681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8681@example.com", "threshold": 810}},
    {"id": "EMAIL-8682", "title": "Email scenario 8682", "data": {"sku": "SKU8682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8682@example.com", "threshold": 820}},
    {"id": "EMAIL-8683", "title": "Email scenario 8683", "data": {"sku": "SKU8683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8683@example.com", "threshold": 830}},
    {"id": "EMAIL-8684", "title": "Email scenario 8684", "data": {"sku": "SKU8684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8684@example.com", "threshold": 840}},
    {"id": "EMAIL-8685", "title": "Email scenario 8685", "data": {"sku": "SKU8685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8685@example.com", "threshold": 850}},
    {"id": "EMAIL-8686", "title": "Email scenario 8686", "data": {"sku": "SKU8686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8686@example.com", "threshold": 860}},
    {"id": "EMAIL-8687", "title": "Email scenario 8687", "data": {"sku": "SKU8687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8687@example.com", "threshold": 870}},
    {"id": "EMAIL-8688", "title": "Email scenario 8688", "data": {"sku": "SKU8688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8688@example.com", "threshold": 880}},
    {"id": "EMAIL-8689", "title": "Email scenario 8689", "data": {"sku": "SKU8689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8689@example.com", "threshold": 890}},
    {"id": "EMAIL-8690", "title": "Email scenario 8690", "data": {"sku": "SKU8690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8690@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
