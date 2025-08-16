import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4741", "title": "Checkout scenario 4741", "data": {"sku": "SKU4741", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4741@example.com", "threshold": 410}},
    {"id": "CHECKOUT-4742", "title": "Checkout scenario 4742", "data": {"sku": "SKU4742", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4742@example.com", "threshold": 420}},
    {"id": "CHECKOUT-4743", "title": "Checkout scenario 4743", "data": {"sku": "SKU4743", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4743@example.com", "threshold": 430}},
    {"id": "CHECKOUT-4744", "title": "Checkout scenario 4744", "data": {"sku": "SKU4744", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4744@example.com", "threshold": 440}},
    {"id": "CHECKOUT-4745", "title": "Checkout scenario 4745", "data": {"sku": "SKU4745", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4745@example.com", "threshold": 450}},
    {"id": "CHECKOUT-4746", "title": "Checkout scenario 4746", "data": {"sku": "SKU4746", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4746@example.com", "threshold": 460}},
    {"id": "CHECKOUT-4747", "title": "Checkout scenario 4747", "data": {"sku": "SKU4747", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4747@example.com", "threshold": 470}},
    {"id": "CHECKOUT-4748", "title": "Checkout scenario 4748", "data": {"sku": "SKU4748", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4748@example.com", "threshold": 480}},
    {"id": "CHECKOUT-4749", "title": "Checkout scenario 4749", "data": {"sku": "SKU4749", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4749@example.com", "threshold": 490}},
    {"id": "CHECKOUT-4750", "title": "Checkout scenario 4750", "data": {"sku": "SKU4750", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4750@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
