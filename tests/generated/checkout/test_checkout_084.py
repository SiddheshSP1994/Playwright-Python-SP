import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4981", "title": "Checkout scenario 4981", "data": {"sku": "SKU4981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4981@example.com", "threshold": 810}},
    {"id": "CHECKOUT-4982", "title": "Checkout scenario 4982", "data": {"sku": "SKU4982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4982@example.com", "threshold": 820}},
    {"id": "CHECKOUT-4983", "title": "Checkout scenario 4983", "data": {"sku": "SKU4983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4983@example.com", "threshold": 830}},
    {"id": "CHECKOUT-4984", "title": "Checkout scenario 4984", "data": {"sku": "SKU4984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4984@example.com", "threshold": 840}},
    {"id": "CHECKOUT-4985", "title": "Checkout scenario 4985", "data": {"sku": "SKU4985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4985@example.com", "threshold": 850}},
    {"id": "CHECKOUT-4986", "title": "Checkout scenario 4986", "data": {"sku": "SKU4986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4986@example.com", "threshold": 860}},
    {"id": "CHECKOUT-4987", "title": "Checkout scenario 4987", "data": {"sku": "SKU4987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4987@example.com", "threshold": 870}},
    {"id": "CHECKOUT-4988", "title": "Checkout scenario 4988", "data": {"sku": "SKU4988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4988@example.com", "threshold": 880}},
    {"id": "CHECKOUT-4989", "title": "Checkout scenario 4989", "data": {"sku": "SKU4989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4989@example.com", "threshold": 890}},
    {"id": "CHECKOUT-4990", "title": "Checkout scenario 4990", "data": {"sku": "SKU4990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4990@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
