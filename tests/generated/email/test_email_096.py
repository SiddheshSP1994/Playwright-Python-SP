import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5741", "title": "Email scenario 5741", "data": {"sku": "SKU5741", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5741@example.com", "threshold": 410}},
    {"id": "EMAIL-5742", "title": "Email scenario 5742", "data": {"sku": "SKU5742", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5742@example.com", "threshold": 420}},
    {"id": "EMAIL-5743", "title": "Email scenario 5743", "data": {"sku": "SKU5743", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5743@example.com", "threshold": 430}},
    {"id": "EMAIL-5744", "title": "Email scenario 5744", "data": {"sku": "SKU5744", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5744@example.com", "threshold": 440}},
    {"id": "EMAIL-5745", "title": "Email scenario 5745", "data": {"sku": "SKU5745", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5745@example.com", "threshold": 450}},
    {"id": "EMAIL-5746", "title": "Email scenario 5746", "data": {"sku": "SKU5746", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5746@example.com", "threshold": 460}},
    {"id": "EMAIL-5747", "title": "Email scenario 5747", "data": {"sku": "SKU5747", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5747@example.com", "threshold": 470}},
    {"id": "EMAIL-5748", "title": "Email scenario 5748", "data": {"sku": "SKU5748", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5748@example.com", "threshold": 480}},
    {"id": "EMAIL-5749", "title": "Email scenario 5749", "data": {"sku": "SKU5749", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5749@example.com", "threshold": 490}},
    {"id": "EMAIL-5750", "title": "Email scenario 5750", "data": {"sku": "SKU5750", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5750@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
