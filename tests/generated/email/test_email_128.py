import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7661", "title": "Email scenario 7661", "data": {"sku": "SKU7661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7661@example.com", "threshold": 610}},
    {"id": "EMAIL-7662", "title": "Email scenario 7662", "data": {"sku": "SKU7662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7662@example.com", "threshold": 620}},
    {"id": "EMAIL-7663", "title": "Email scenario 7663", "data": {"sku": "SKU7663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7663@example.com", "threshold": 630}},
    {"id": "EMAIL-7664", "title": "Email scenario 7664", "data": {"sku": "SKU7664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7664@example.com", "threshold": 640}},
    {"id": "EMAIL-7665", "title": "Email scenario 7665", "data": {"sku": "SKU7665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7665@example.com", "threshold": 650}},
    {"id": "EMAIL-7666", "title": "Email scenario 7666", "data": {"sku": "SKU7666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7666@example.com", "threshold": 660}},
    {"id": "EMAIL-7667", "title": "Email scenario 7667", "data": {"sku": "SKU7667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7667@example.com", "threshold": 670}},
    {"id": "EMAIL-7668", "title": "Email scenario 7668", "data": {"sku": "SKU7668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7668@example.com", "threshold": 680}},
    {"id": "EMAIL-7669", "title": "Email scenario 7669", "data": {"sku": "SKU7669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7669@example.com", "threshold": 690}},
    {"id": "EMAIL-7670", "title": "Email scenario 7670", "data": {"sku": "SKU7670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7670@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
