import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8741", "title": "Email scenario 8741", "data": {"sku": "SKU8741", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8741@example.com", "threshold": 410}},
    {"id": "EMAIL-8742", "title": "Email scenario 8742", "data": {"sku": "SKU8742", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8742@example.com", "threshold": 420}},
    {"id": "EMAIL-8743", "title": "Email scenario 8743", "data": {"sku": "SKU8743", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8743@example.com", "threshold": 430}},
    {"id": "EMAIL-8744", "title": "Email scenario 8744", "data": {"sku": "SKU8744", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8744@example.com", "threshold": 440}},
    {"id": "EMAIL-8745", "title": "Email scenario 8745", "data": {"sku": "SKU8745", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8745@example.com", "threshold": 450}},
    {"id": "EMAIL-8746", "title": "Email scenario 8746", "data": {"sku": "SKU8746", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8746@example.com", "threshold": 460}},
    {"id": "EMAIL-8747", "title": "Email scenario 8747", "data": {"sku": "SKU8747", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8747@example.com", "threshold": 470}},
    {"id": "EMAIL-8748", "title": "Email scenario 8748", "data": {"sku": "SKU8748", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8748@example.com", "threshold": 480}},
    {"id": "EMAIL-8749", "title": "Email scenario 8749", "data": {"sku": "SKU8749", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8749@example.com", "threshold": 490}},
    {"id": "EMAIL-8750", "title": "Email scenario 8750", "data": {"sku": "SKU8750", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8750@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
