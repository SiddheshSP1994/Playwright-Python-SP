import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0761", "title": "Email scenario 761", "data": {"sku": "SKU761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user761@example.com", "threshold": 610}},
    {"id": "EMAIL-0762", "title": "Email scenario 762", "data": {"sku": "SKU762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user762@example.com", "threshold": 620}},
    {"id": "EMAIL-0763", "title": "Email scenario 763", "data": {"sku": "SKU763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user763@example.com", "threshold": 630}},
    {"id": "EMAIL-0764", "title": "Email scenario 764", "data": {"sku": "SKU764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user764@example.com", "threshold": 640}},
    {"id": "EMAIL-0765", "title": "Email scenario 765", "data": {"sku": "SKU765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user765@example.com", "threshold": 650}},
    {"id": "EMAIL-0766", "title": "Email scenario 766", "data": {"sku": "SKU766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user766@example.com", "threshold": 660}},
    {"id": "EMAIL-0767", "title": "Email scenario 767", "data": {"sku": "SKU767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user767@example.com", "threshold": 670}},
    {"id": "EMAIL-0768", "title": "Email scenario 768", "data": {"sku": "SKU768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user768@example.com", "threshold": 680}},
    {"id": "EMAIL-0769", "title": "Email scenario 769", "data": {"sku": "SKU769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user769@example.com", "threshold": 690}},
    {"id": "EMAIL-0770", "title": "Email scenario 770", "data": {"sku": "SKU770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user770@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
