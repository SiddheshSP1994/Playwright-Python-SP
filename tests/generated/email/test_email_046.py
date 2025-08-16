import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2741", "title": "Email scenario 2741", "data": {"sku": "SKU2741", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2741@example.com", "threshold": 410}},
    {"id": "EMAIL-2742", "title": "Email scenario 2742", "data": {"sku": "SKU2742", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2742@example.com", "threshold": 420}},
    {"id": "EMAIL-2743", "title": "Email scenario 2743", "data": {"sku": "SKU2743", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2743@example.com", "threshold": 430}},
    {"id": "EMAIL-2744", "title": "Email scenario 2744", "data": {"sku": "SKU2744", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2744@example.com", "threshold": 440}},
    {"id": "EMAIL-2745", "title": "Email scenario 2745", "data": {"sku": "SKU2745", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2745@example.com", "threshold": 450}},
    {"id": "EMAIL-2746", "title": "Email scenario 2746", "data": {"sku": "SKU2746", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2746@example.com", "threshold": 460}},
    {"id": "EMAIL-2747", "title": "Email scenario 2747", "data": {"sku": "SKU2747", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2747@example.com", "threshold": 470}},
    {"id": "EMAIL-2748", "title": "Email scenario 2748", "data": {"sku": "SKU2748", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2748@example.com", "threshold": 480}},
    {"id": "EMAIL-2749", "title": "Email scenario 2749", "data": {"sku": "SKU2749", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2749@example.com", "threshold": 490}},
    {"id": "EMAIL-2750", "title": "Email scenario 2750", "data": {"sku": "SKU2750", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2750@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
